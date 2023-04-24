from kalman import Kalman
import numpy as np
from scipy.optimize import linear_sum_assignment


class SortTracker:
	def __init__(self, age=4, hits=1, iou_thrd=0.3):
		self.tracker_list = []
		self.tracked_boxes = []  # x_box
		self.max_age = age
		self.min_hits = hits
		self.iou_thrd = iou_thrd
		self.max_index = 0

	def predict(self, prediction_boxes: np.ndarray):
		matches, unmatched_detections, unmatched_trackers = self.estimate_hungarian(prediction_boxes)

		if matches.size > 0:
			for trk_idx, det_idx in matches:
				pred = prediction_boxes[det_idx]
				pred = np.expand_dims(pred, axis=0).T
				tmp_trk = self.tracker_list[trk_idx]
				tmp_trk.kalman_filter(pred)
				xx = tmp_trk.x_state.T[0].tolist()
				xx = [xx[0], xx[2], xx[4], xx[6]]
				self.tracked_boxes[trk_idx] = xx
				tmp_trk.last_box = pred.reshape((4))
				tmp_trk.box = xx
				tmp_trk.hits += 1
				tmp_trk.no_losses = 0

		if len(unmatched_detections) > 0:
			for idx in unmatched_detections:
				pred = prediction_boxes[idx]
				pred = np.expand_dims(pred, axis=0).T
				tmp_trk = Kalman()  # Create a new tracker
				x = np.array([[pred[0], 0, pred[1], 0, pred[2], 0, pred[3], 0]]).T
				tmp_trk.x_state = x
				tmp_trk.predict_only()
				xx = tmp_trk.x_state
				xx = xx.T[0].tolist()
				xx = [xx[0], xx[2], xx[4], xx[6]]
				tmp_trk.box = xx
				tmp_trk.id = self.max_index  # assign an ID for the tracker
				self.max_index += 1
				self.tracker_list.append(tmp_trk)
				self.tracked_boxes.append(xx)

		if len(unmatched_trackers) > 0:
			for trk_idx in unmatched_trackers:
				tmp_trk = self.tracker_list[trk_idx]
				tmp_trk.no_losses += 1
				tmp_trk.predict_only()
				xx = tmp_trk.x_state
				xx = xx.T[0].tolist()
				xx = [xx[0], xx[2], xx[4], xx[6]]
				tmp_trk.box = xx
				self.tracked_boxes[trk_idx] = xx

		new_state = []
		good_tracker_list = []
		for trk in self.tracker_list:
			if (trk.hits >= self.min_hits) and (trk.no_losses <= self.max_age):
				new_state.append({"track_id": trk.id, "bbox": trk.last_box})
				good_tracker_list.append(trk)

		self.tracker_list = [x for x in self.tracker_list if x.no_losses <= self.max_age]
		filter(lambda x: x.no_losses > self.max_age, self.tracker_list)
		return new_state

	def get_trackers_boxes(self):
		boxes = []
		for tracker in self.tracker_list:
			boxes.append(tracker.box)
		return np.array(boxes)

	def get_iou(self, pred_box):
		tracker_boxes = self.get_trackers_boxes()
		if tracker_boxes.size == 0 or len(pred_box) == 0:
			return np.zeros((len(pred_box), len(tracker_boxes)), dtype=np.float32)
		x11, y11, x12, y12 = np.split(pred_box, 4, axis=1)
		x21, y21, x22, y22 = np.split(tracker_boxes, 4, axis=1)
		x_a = np.maximum(x11, np.transpose(x21))
		y_a = np.maximum(y11, np.transpose(y21))
		x_b = np.minimum(x12, np.transpose(x22))
		y_b = np.minimum(y12, np.transpose(y22))
		inter_area = np.maximum((x_b - x_a + 1), 0) * np.maximum((y_b - y_a + 1), 0)
		box_area_a = (x12 - x11 + 1) * (y12 - y11 + 1)
		box_area_b = (x22 - x21 + 1) * (y22 - y21 + 1)
		return inter_area / (box_area_a + np.transpose(box_area_b) - inter_area)

	def estimate_hungarian(self, pred_box):
		iou_table = self.get_iou(pred_box)

		row_ind, col_ind = linear_sum_assignment(iou_table, maximize=True)

		rows, cols = iou_table.shape

		unmatched_detections = set(range(0, rows)).difference(row_ind)
		unmatched_trackers = set(range(0, cols)).difference(col_ind)

		mask = iou_table[row_ind, col_ind] < self.iou_thrd
		unmatched_detections.update(row_ind[mask])
		unmatched_trackers.update(col_ind[mask])

		matches = np.stack([col_ind, row_ind], axis=1)[~mask]
		return matches, np.array(list(unmatched_detections)), np.array(list(unmatched_trackers))
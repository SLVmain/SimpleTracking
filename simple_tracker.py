import numpy as np
from scipy.optimize import linear_sum_assignment
from kalman import Kalman

eps = 1e-6
iou_thrd = 0.2


class SimpleTracker:
	def __init__(self):
		self.max_index = 0
		self.iou_table = None
		# [{"track_id" : 1, "bbox": [1,2,3,4]},
		#  {"track_id" : 2, "bbox": [1,2,3,7]},
		#  ...]
		self.previous_state = []
		self.previous_state_boxes = None
		self.kalman_info = []

	def initialize(self, data: np.ndarray):
		self.previous_state_boxes = data
		for i in range(data.shape[0]):
			self.previous_state.append({"track_id": self.max_index, "bbox": data[i]})
			self.max_index += 1


	def update_states(self, boxes, matches, unmatched_detections):
		self.previous_state_boxes = []
		new_state = []
		for track_idx, det_idx in matches:
			new_state.append({"track_id": self.previous_state[track_idx]['track_id'], "bbox": boxes[det_idx]})
			self.previous_state_boxes.append(boxes[det_idx])
		for ud in unmatched_detections.tolist():
			new_state.append({"track_id": self.max_index, "bbox": boxes[ud]})
			self.previous_state_boxes.append(boxes[ud])
			self.max_index += 1
		self.previous_state = new_state
		self.previous_state_boxes = np.stack(self.previous_state_boxes)
		return new_state

	def get_iou(self, pred_box):
		x11, y11, x12, y12 = np.split(pred_box, 4, axis=1)
		x21, y21, x22, y22 = np.split(self.previous_state_boxes, 4, axis=1)
		x_a = np.maximum(x11, np.transpose(x21))
		y_a = np.maximum(y11, np.transpose(y21))
		x_b = np.minimum(x12, np.transpose(x22))
		y_b = np.minimum(y12, np.transpose(y22))
		inter_area = np.maximum((x_b - x_a + 1), 0) * np.maximum((y_b - y_a + 1), 0)
		box_area_a = (x12 - x11 + 1) * (y12 - y11 + 1)
		box_area_b = (x22 - x21 + 1) * (y22 - y21 + 1)
		self.iou_table = inter_area / (box_area_a + np.transpose(box_area_b) - inter_area)

	def estimate_hungarian(self):
		row_ind, col_ind = linear_sum_assignment(self.iou_table, maximize=True)

		rows, cols = self.iou_table.shape

		unmatched_detections = set(range(0, rows)).difference(row_ind)
		unmatched_trackers = set(range(0, cols)).difference(col_ind)

		# For creating trackers we consider any detection with an
		# overlap less than iou_thrd to signifiy the existence of
		# an untracked object

		mask = self.iou_table[row_ind, col_ind] < iou_thrd
		unmatched_detections.update(row_ind[mask])
		unmatched_trackers.update(col_ind[mask])

		matches = np.stack([col_ind, row_ind], axis=1)[~mask]
		return matches, np.array(unmatched_detections), np.array(unmatched_trackers)

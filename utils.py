import numpy as np


def extract_boxes(data: list):
	boxes = [(i, data[i]['bounding_box']) for i in range(len(data)) if len(data[i]['bounding_box']) != 0]
	res = list(zip(*boxes))
	if len(res) == 0:  # 0 non-empty boxes
		return [], []
	return dict(enumerate(res[0])), np.array(res[1])


def from_tracker(service_data, tracker_data: list, mapping: dict):
	for index_tracker, index_service in mapping.items():
		service_data[index_service]['track_id'] = tracker_data[index_tracker]['track_id']
		service_data[index_service]['bounding_box'] = tracker_data[index_tracker]['bbox'].tolist()
	return service_data

import numpy as np
from scipy.linalg import inv, block_diag


# taken from https://github.com/kcg2015/Vehicle-Detection-and-Tracking
class Kalman:  # class for Kalman Filter-based tracker
	def __init__(self):
		# Initialize parametes for tracker (history)
		self.id = 0  # tracker's id
		self.box = []  # list to store the coordinates for a bounding box
		self.hits = 0  # number of detection matches
		self.no_losses = 0  # number of unmatched tracks (track loss)
		self.last_box = []  # last passed box to tracker
		# Initialize parameters for Kalman Filtering
		# The state is the (x, y) coordinates of the detection box
		# state: [up, up_dot, left, left_dot, down, down_dot, right, right_dot]
		# or[up, up_dot, left, left_dot, height, height_dot, width, width_dot]
		self.x_state = []
		self.dt = 1.  # time interval

		# Process matrix, assuming constant velocity model
		self.F = np.array([[1, self.dt, 0, 0, 0, 0, 0, 0],
						   [0, 1, 0, 0, 0, 0, 0, 0],
						   [0, 0, 1, self.dt, 0, 0, 0, 0],
						   [0, 0, 0, 1, 0, 0, 0, 0],
						   [0, 0, 0, 0, 1, self.dt, 0, 0],
						   [0, 0, 0, 0, 0, 1, 0, 0],
						   [0, 0, 0, 0, 0, 0, 1, self.dt],
						   [0, 0, 0, 0, 0, 0, 0, 1]])

		# Measurement matrix, assuming we can only measure the coordinates

		self.H = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 1, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 1, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0, 1, 0]])

		# Initialize the state covariance
		self.L = 10.0
		self.P = np.diag(self.L * np.ones(8))

		# Initialize the process covariance
		self.Q_comp_mat = np.array([[self.dt ** 4 / 4., self.dt ** 3 / 2.],
									[self.dt ** 3 / 2., self.dt ** 2]])
		self.Q = block_diag(self.Q_comp_mat, self.Q_comp_mat,
							self.Q_comp_mat, self.Q_comp_mat)

		# Initialize the measurement covariance
		self.R_scaler = 1.0
		self.R_diag_array = self.R_scaler * np.array([self.L, self.L, self.L, self.L])
		self.R = np.diag(self.R_diag_array)

	def update_R(self):
		R_diag_array = self.R_scaler * np.array([self.L, self.L, self.L, self.L])
		self.R = np.diag(R_diag_array)

	def kalman_filter(self, z):
		'''
		Implement the Kalman Filter, including the prediction and the update stages,
		with the measurement z
		'''
		x = self.x_state
		# Predict
		x = np.dot(self.F, x)
		self.P = np.dot(self.F, self.P).dot(self.F.T) + self.Q

		# Update
		S = np.dot(self.H, self.P).dot(self.H.T) + self.R
		K = np.dot(self.P, self.H.T).dot(inv(S))  # Kalman gain
		y = z - np.dot(self.H, x)  # residual
		x += np.dot(K, y)
		self.P = self.P - np.dot(K, self.H).dot(self.P)
		self.x_state = x.astype(int)  # convert to integer coordinates

	# (pixel values)

	def predict_only(self):
		'''
		Implment only the predict stage. This is used for unmatched detections and
		unmatched tracks
		'''
		x = self.x_state
		# Predict
		x = np.dot(self.F, x)
		self.P = np.dot(self.F, self.P).dot(self.F.T) + self.Q
		self.x_state = x.astype(int)
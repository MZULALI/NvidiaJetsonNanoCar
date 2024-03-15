# camera_utils.py

import cv2
import yaml

class CameraUtils:
    def __init__(self):
        self.cap = None
        self.load_camera_params()

    def load_camera_params(self):
        with open('../config/camera_params.yaml', 'r') as file:
            self.camera_params = yaml.safe_load(file)

    def open_camera(self):
        camera_id = self.camera_params['camera_id']
        self.cap = cv2.VideoCapture(camera_id)
        if not self.cap.isOpened():
            rospy.logerr("Failed to open camera!")
            return False
        rospy.loginfo("Camera opened successfully.")
        return True

    def capture_frame(self):
        if self.cap is None:
            rospy.logerr("Camera is not initialized!")
            return None

        ret, frame = self.cap.read()
        if not ret:
            rospy.logerr("Failed to capture frame from camera!")
            return None

        return frame

    def release_camera(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None
            rospy.loginfo("Camera released.")

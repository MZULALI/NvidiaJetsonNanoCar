# camera_node.py

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from camera_utils import CameraUtils

class CameraNode:
    def __init__(self):
        rospy.init_node('camera_node', anonymous=True)
        self.image_pub = rospy.Publisher('/camera/image', Image, queue_size=1)
        self.bridge = CvBridge()
        self.camera = CameraUtils()
        self.camera.open_camera()

    def run(self):
        rate = rospy.Rate(30)  # 30 Hz
        while not rospy.is_shutdown():
            frame = self.camera.capture_frame()
            if frame is not None:
                image_msg = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
                self.image_pub.publish(image_msg)
            rate.sleep()

if __name__ == '__main__':
    try:
        camera_node = CameraNode()
        camera_node.run()
    except rospy.ROSInterruptException:
        pass

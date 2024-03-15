# object_detection_node.py

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from object_detection_model import ObjectDetectionModel
from object_detection_utils import visualize_detections
from std_msgs.msg import String

class ObjectDetectionNode:
    def __init__(self):
        rospy.init_node('object_detection_node', anonymous=True)
        self.bridge = CvBridge()
        self.object_detection_model = ObjectDetectionModel()
        self.image_sub = rospy.Subscriber('/camera/image', Image, self.image_callback)
        self.detections_pub = rospy.Publisher('/object_detection/detections', String, queue_size=1)

    def image_callback(self, image_msg):
        image = self.bridge.imgmsg_to_cv2(image_msg, desired_encoding='bgr8')
        detections = self.object_detection_model.detect_objects(image)
        self.publish_detections(detections)
        visualize_detections(image, detections)

    def publish_detections(self, detections):
        detections_msg = String()
        detections_msg.data = str(detections)
        self.detections_pub.publish(detections_msg)

if __name__ == '__main__':
    try:
        object_detection_node = ObjectDetectionNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

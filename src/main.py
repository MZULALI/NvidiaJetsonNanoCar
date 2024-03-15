# main.py

import rospy
from camera.camera_node import CameraNode
from object_detection.object_detection_node import ObjectDetectionNode
from control.control_node import ControlNode

def main():
    rospy.init_node('self_driving_car', anonymous=True)

    try:
        camera_node = CameraNode()
        object_detection_node = ObjectDetectionNode()
        control_node = ControlNode()

        rospy.loginfo("Self-driving car nodes initialized.")

        camera_node.run()
        rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("Self-driving car program terminated.")

if __name__ == '__main__':
    main()

# control_node.py

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from control_utils import ControlUtils

class ControlNode:
    def __init__(self):
        rospy.init_node('control_node', anonymous=True)
        self.control_utils = ControlUtils()
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.detections_sub = rospy.Subscriber('/object_detection/detections', String, self.detections_callback)

    def detections_callback(self, detections_msg):
        detections = eval(detections_msg.data)
        control_command = self.control_utils.generate_control_command(detections)
        self.publish_control_command(control_command)

    def publish_control_command(self, control_command):
        cmd_vel_msg = Twist()
        cmd_vel_msg.linear.x = control_command['linear_velocity']
        cmd_vel_msg.angular.z = control_command['angular_velocity']
        self.cmd_vel_pub.publish(cmd_vel_msg)

if __name__ == '__main__':
    try:
        control_node = ControlNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

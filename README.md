# Self-Driving Car

This is a ROS package for a self-driving toy car using the Nvidia Jetson Nano. It utilizes a camera sensor for perception and performs object detection and obstacle avoidance.

## Prerequisites

- Nvidia Jetson Nano
- ROS (Robot Operating System)
- Python 3.6+
- TensorFlow 2.5+
- OpenCV 4.5+

## Installation

1. Clone this repository to your ROS workspace:cd ~/catkin_ws/src
git clone https://github.com/your-username/self-driving-car.git

2. Install the required dependencies:
cd ~/catkin_ws/src/self-driving-car
pip install -r requirements.txt

3. Build the ROS package:
cd ~/catkin_ws
catkin_make

## Usage

1. Launch the self-driving car nodes:
roslaunch self_driving_car self_driving_car.launch

This will start the camera node, object detection node, and control node.

2. Visualize the camera feed and object detection results:
rosrun image_view image_view image:=/camera/image
rosrun image_view image_view image:=/object_detection/image

3. View the control commands:
rostopic echo /cmd_vel

## Configuration

- `config/camera_params.yaml`: Camera configuration parameters.
- `config/object_detection_params.yaml`: Object detection model and settings.
- `config/control_params.yaml`: Control parameters for obstacle avoidance.

## ROS Nodes

- `camera_node`: Captures images from the camera sensor and publishes them to the `/camera/image` topic.
- `object_detection_node`: Performs object detection on the camera images and publishes the results to the `/object_detection/detections` topic.
- `control_node`: Generates control commands based on the detected objects and publishes them to the `/cmd_vel` topic.

## ROS Topics

- `/camera/image`: Published by the `camera_node`, containing the camera images.
- `/object_detection/detections`: Published by the `object_detection_node`, containing the detected objects.
- `/cmd_vel`: Published by the `control_node`, containing the control commands for the car.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
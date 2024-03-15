# control_utils.py

import yaml

class ControlUtils:
    def __init__(self):
        self.load_control_params()

    def load_control_params(self):
        with open('../config/control_params.yaml', 'r') as file:
            self.control_params = yaml.safe_load(file)

    def generate_control_command(self, detections):
        # Customize this function based on your specific control logic
        # This is just a placeholder example

        linear_velocity = 0.0
        angular_velocity = 0.0

        if len(detections) > 0:
            # Example: Stop the car if an object is detected close to the car
            min_distance = self.control_params['min_distance']
            for detection in detections:
                if detection['class_name'] in ['person', 'car', 'truck']:
                    xmin, ymin, xmax, ymax = detection['box']
                    distance = (ymax - ymin) / 2.0  # Approximate distance based on bounding box height
                    if distance < min_distance:
                        linear_velocity = 0.0
                        angular_velocity = 0.0
                        break
            else:
                # Example: Move forward if no close objects are detected
                linear_velocity = self.control_params['default_linear_velocity']
                angular_velocity = 0.0
        else:
            # Example: Rotate in place if no objects are detected
            linear_velocity = 0.0
            angular_velocity = self.control_params['default_angular_velocity']

        control_command = {
            'linear_velocity': linear_velocity,
            'angular_velocity': angular_velocity
        }

        return control_command

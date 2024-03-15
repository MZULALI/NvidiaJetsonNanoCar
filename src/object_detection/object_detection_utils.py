# object_detection_utils.py

import cv2

def visualize_detections(image, detections):
    for detection in detections:
        xmin, ymin, xmax, ymax = detection['box']
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
        class_name = detection['class_name']
        score = detection['score']
        label = f'{class_name}: {score:.2f}'
        cv2.putText(image, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Object Detection', image)
    cv2.waitKey(1)

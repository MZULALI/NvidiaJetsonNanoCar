# object_detection_model.py

import tensorflow as tf
import numpy as np

class ObjectDetectionModel:
    def __init__(self):
        self.model = self.load_model()
        self.class_names = self.load_class_names()

    def load_model(self):
        model_path = '../models/ssd_mobilenet_v2_coco.pb'
        detection_graph = tf.Graph()
        with detection_graph.as_default():
            od_graph_def = tf.compat.v1.GraphDef()
            with tf.compat.v1.gfile.GFile(model_path, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
        return detection_graph

    def load_class_names(self):
        class_names = ['background', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck',
                       'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
                       'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack',
                       'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
                       'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
                       'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
                       'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair',
                       'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
                       'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book',
                       'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']
        return class_names

    def detect_objects(self, image):
        with self.model.as_default():
            with tf.compat.v1.Session(graph=self.model) as sess:
                image_tensor = self.model.get_tensor_by_name('image_tensor:0')
                detection_boxes = self.model.get_tensor_by_name('detection_boxes:0')
                detection_scores = self.model.get_tensor_by_name('detection_scores:0')
                detection_classes = self.model.get_tensor_by_name('detection_classes:0')
                num_detections = self.model.get_tensor_by_name('num_detections:0')

                image_np_expanded = np.expand_dims(image, axis=0)
                (boxes, scores, classes, num) = sess.run(
                    [detection_boxes, detection_scores, detection_classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})

                detections = []
                for i in range(int(num[0])):
                    if scores[0][i] > 0.5:
                        class_id = int(classes[0][i])
                        class_name = self.class_names[class_id]
                        box = boxes[0][i]
                        ymin, xmin, ymax, xmax = box
                        detections.append({
                            'class_id': class_id,
                            'class_name': class_name,
                            'score': scores[0][i],
                            'box': (int(xmin * image.shape[1]), int(ymin * image.shape[0]),
                                    int(xmax * image.shape[1]), int(ymax * image.shape[0]))
                        })

                return detections

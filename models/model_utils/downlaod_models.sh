#!/bin/bash

# Download object detection models
wget http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz -P models/object_detection/ssd_mobilenet_v2_coco/
wget http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz -P models/object_detection/faster_rcnn_inception_v2_coco/
wget http://download.tensorflow.org/models/object_detection/mask_rcnn_inception_v2_coco_2018_01_28.tar.gz -P models/object_detection/mask_rcnn_inception_v2_coco/

# Extract object detection models
tar -xvf models/object_detection/ssd_mobilenet_v2_coco/ssd_mobilenet_v2_coco_2018_03_29.tar.gz -C models/object_detection/ssd_mobilenet_v2_coco/
tar -xvf models/object_detection/faster_rcnn_inception_v2_coco/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz -C models/object_detection/faster_rcnn_inception_v2_coco/
tar -xvf models/object_detection/mask_rcnn_inception_v2_coco/mask_rcnn_inception_v2_coco_2018_01_28.tar.gz -C models/object_detection/mask_rcnn_inception_v2_coco/

# Download lane detection models
wget https://example.com/lane_detection/erfnet/model.pb -P models/lane_detection/erfnet/
wget https://example.com/lane_detection/erfnet/model.ckpt -P models/lane_detection/erfnet/
wget https://example.com/lane_detection/unet/model.pb -P models/lane_detection/unet/
wget https://example.com/lane_detection/unet/model.ckpt -P models/lane_detection/unet/

# Download traffic sign classification models
wget https://example.com/traffic_sign_classification/inception_v3/model.pb -P models/traffic_sign_classification/inception_v3/
wget https://example.com/traffic_sign_classification/inception_v3/model.ckpt -P models/traffic_sign_classification/inception_v3/
wget https://example.com/traffic_sign_classification/mobilenet_v2/model.pb -P models/traffic_sign_classification/mobilenet_v2/
wget https://example.com/traffic_sign_classification/mobilenet_v2/model.ckpt -P models/traffic_sign_classification/mobilenet_v2/

# Download depth estimation models
wget https://example.com/depth_estimation/monodepth2/model.pb -P models/depth_estimation/monodepth2/
wget https://example.com/depth_estimation/monodepth2/model.ckpt -P models/depth_estimation/monodepth2/
wget https://example.com/depth_estimation/pydnet/model.pb -P models/depth_estimation/pydnet/
wget https://example.com/depth_estimation/pydnet/model.ckpt -P models/depth_estimation/pydnet/

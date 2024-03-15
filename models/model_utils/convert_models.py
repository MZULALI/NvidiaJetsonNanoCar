import tensorflow as tf
from tensorflow.python.framework import graph_util
from tensorflow.python.platform import gfile

def convert_model(model_dir, output_node_names):
    with tf.Session() as sess:
        # Load the saved model
        model_path = f"{model_dir}/model.ckpt"
        saver = tf.train.import_meta_graph(f"{model_path}.meta")
        saver.restore(sess, model_path)

        # Get the graph
        graph = tf.get_default_graph()

        # Convert variables to constants
        output_graph_def = graph_util.convert_variables_to_constants(
            sess,
            graph.as_graph_def(),
            output_node_names
        )

        # Save the frozen graph
        output_path = f"{model_dir}/frozen_model.pb"
        with gfile.GFile(output_path, "wb") as f:
            f.write(output_graph_def.SerializeToString())

        print(f"Converted model saved to: {output_path}")

# Convert object detection models
convert_model("models/object_detection/ssd_mobilenet_v2_coco", ["detection_boxes", "detection_scores", "detection_classes", "num_detections"])
convert_model("models/object_detection/faster_rcnn_inception_v2_coco", ["detection_boxes", "detection_scores", "detection_classes", "num_detections"])
convert_model("models/object_detection/mask_rcnn_inception_v2_coco", ["detection_boxes", "detection_scores", "detection_classes", "detection_masks", "num_detections"])

# Convert lane detection models
convert_model("models/lane_detection/erfnet", ["output"])
convert_model("models/lane_detection/unet", ["output"])

# Convert traffic sign classification models
convert_model("models/traffic_sign_classification/inception_v3", ["output"])
convert_model("models/traffic_sign_classification/mobilenet_v2", ["output"])

# Convert depth estimation models
convert_model("models/depth_estimation/monodepth2", ["output"])
convert_model("models/depth_estimation/pydnet", ["output"])

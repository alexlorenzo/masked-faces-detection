# Tensorflow API implementation

## 1. Configuration
 - First you need to export your images labelled as tensorflow format, then you will have “.pbtxt” file / “.tfrecord” files with training and validation
- git clone [https://github.com/tensorflow/models](https://github.com/tensorflow/models/tree/master/research/object_detection)
*Remarks: You will find all necessary Python codes for the Tensorflow API in: [https://github.com/tensorflow/models/research/object_detection](https://github.com/tensorflow/models/tree/master/research/object_detection)

- Load the model you need (e.g. [faster_rcnn_inception_v2_coco_2018_01_28.tar.gz](http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz))  [https://docs.openvinotoolkit.org/2018_R5/_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_TensorFlow.html](https://docs.openvinotoolkit.org/2018_R5/_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_TensorFlow.html)
- Load the model config you want in (e.g. [faster_rcnn_inception_v2_pets.con](https://github.com/tensorflow/models/blob/master/research/object_detection/samples/configs/faster_rcnn_inception_v2_pets.config "faster_rcnn_inception_v2_pets.config")fig) : [https://github.com/tensorflow/models/tree/master/research/object_detection/samples/configs](https://github.com/tensorflow/models/tree/master/research/object_detection/samples/configs) (following models are available: SSD, fasterRCNN, MaskRCNN)
- Modify the config as follow:
	- Modify Line 127 fine_tune_checkpoint: "PATH_TO_BE_CONFIGURED/model.ckpt"
	- Modify Line 142: “PATH_TO_BE_CONFIGURED/.tfrecord”
	- Modify Line 144: "PATH_TO_BE_CONFIGURED/label_map.pbtxt”
	- Modify Line 158: “PATH_TO_BE_CONFIGURED/.tfrecord” for validation
	-  Modify Line 160: “PATH_TO_BE_CONFIGURED/.pbtxt” for validation
- Go to cd ../models/research/object_detection
- Write export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim  
    
### 2. Launch Model

    python object_detection/model_main.py --pipeline_config_path="/Users/user/Documents/ComputerVision/models/research/object_detection/mask_detection/faster_rcnn_inception_v2_pets.config" --model_dir="/Users/user/Documents/ComputerVision/" —alsologtostderr

### 3. Evaluate Model

    python object_detection/export_inference_graph.py --input_type image_tensor --pipeline_config_path /Users/user/Documents/ComputerVision/masked-faces-detection/data/faster_rcnn_inception_v2_pets.config --trained_checkpoint_prefix /Users/user/Documents/ComputerVision/masked-faces-detection/output/model.ckpt-500.meta --output_directory /Users/user/Documents/ComputerVision/masked-faces-detection/output/inference_graph

- Then test with your model using Evaluate_TensorflowAPI


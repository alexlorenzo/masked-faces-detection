# Mask Detector using YOLOv3

Ultralytics                |  On mask detection(add gif)
:-------------------------:|:-------------------------:
![](https://avatars1.githubusercontent.com/u/26833451?s=280&v=4)  |  ![](https://avatars1.githubusercontent.com/u/26833451?s=280&v=4)


The purpose of this repository its to train your own YOLO model on new datasets for that I provide mask/no mask datasets.

# Requirements
To manage package and dependency easily I used the [poetry](https://python-poetry.org/) package.
Simply use the following command line once you have installed poetry, it will create automatically a .venv folder.
```
$ poetry install 
```
If you have issues installing poetry, check that:
```
$ poetry config --list
```
returns:
```
cache-dir = "/Users/user/Library/Caches/pypoetry"
virtualenvs.create = true
virtualenvs.in-project = true
virtualenvs.path = "{cache-dir}/virtualenvs"
```

If you want to execute the code right away, I added a notebook *Mask_Detection_Yolov3_ultralytics.ipynb* that you can run in Google Colab.

### Repository structure
```
masked-faces-detection
└── yolov3: package from ultralytics yolov3 
    ├── weights (include weights from ultralytics or Kaggle datasets)
└── mask: include datasets (ex: in Kaggle datasets)
    ├── images
    |   └── include jpg files
    ├── labels
        |   └── include txt files
    ├── train.txt
    ├── test.txt
    ├── valid.txt
└── notebooks: some useful notebooks
└── Mask_Detection_Yolov3_ultralytics.ipynb: implementation using Mask Datasets
└── pyproject.toml
└── poetry.lock
└── .gitignore
└── README.md
```
### Reproduce our result
I recommend to follow the Customer [Train Custom Data](https://github.com/ultralytics/yolov3/wiki/Train-Custom-Data) from Ultralytics.
If not, follow the instruction in the notebook from this repository. 

### Datasets

All datasets have been found by scrapping Google images and from the real/fake datasets from  [Kaggle](https://www.kaggle.com/ciplab/real-and-fake-face-detection?).
We have labelled all images using [CVAT](https://github.com/opencv/cvat) package and exporting our result in the YOLO format.
You can find the pre-trained weights (Pytorch format) from the mask detector in the **model** folder.
All the data are available in this [Kaggle datasets](https://www.kaggle.com/alexandralorenzo/maskdetection).



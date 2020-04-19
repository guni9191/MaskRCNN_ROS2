# Mask R-CNN for Object Detection and Segmentation

This is a balloon color splash example of MaskRCNN ported on ROS2 by guni9191. For better understanding, go to https://github.com/matterport/Mask_RCNN.

## Requirements
Python 3.4, TensorFlow 1.3, Keras 2.0.8 and other common packages listed in `requirements.txt`.

## Installation
1. Clone this repository
2. Install dependencies
   ```bash
   pip3 install -r requirements.txt
   ```
3. Run setup from the repository root directory(you might try sudo -s if permission error occurs)
    ```bash
    python3 setup.py install
    ``` 

### [Splash of Color](https://engineering.matterport.com/splash-of-color-instance-segmentation-with-mask-r-cnn-and-tensorflow-7c761e238b46). A blog post explaining how to train this model from scratch and use it to implement a color splash effect.
![Balloon Color Splash](assets/balloon_color_splash.gif)

## Usage
Change your mode, weight file location and input sources in balloon_launch.py in launch folder.

import os

import launch
import launch_ros.actions

from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    ld = launch.LaunchDescription()
    
    balloon_node = Node(
        package = 'mask_rcnn',
        node_executable = 'balloon.py',
        output = 'screen',
        parameters = [
        {'command': 'splash'}, #train or splash
        {'dataset': '/path/to/balloon/dataset/'},
        {'weights': 'balloon'},
        {'weights_path': '/home/psh/ros2_ws/src/Mask_RCNN/samples/balloon/mask_rcnn_balloon.h5'},
        {'logs': '/path/to/logs/'},
        {'image': '/home/psh/ros2_ws/src/Mask_RCNN/samples/balloon/balloon_test.jpg'},
        {'video': 'path or URL to video'},
        ],
    )

    ld.add_action( balloon_node )

    return ld

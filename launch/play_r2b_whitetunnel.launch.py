from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Reproduce el rosbag con --loop
        ExecuteProcess(
            cmd=[
                'ros2', 'bag', 'play',
                '/home/user/r2bdataset2024_v1/r2b_whitetunnel',
                '--loop'
            ],
            output='screen'
        ),

        # Abre RViz
        ExecuteProcess(
            cmd=['rviz2'],
            output='screen'
        ),

        # Abre RQT
        ExecuteProcess(
            cmd=['rqt'],
            output='screen'
        )
    ])

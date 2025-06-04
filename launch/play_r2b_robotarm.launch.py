from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
import os

def generate_launch_description():
    rviz_config_path = os.path.expanduser(
        '~/ros2_ws/src/rincon_charris_pkg/config/robotarm.rviz'
    )

    return LaunchDescription([
        # ▶ Reproduce el rosbag del robot en bucle
        ExecuteProcess(
            cmd=[
                'ros2', 'bag', 'play',
                '/home/user/r2bdataset2024_v1/r2b_robotarm',
                '--loop'
            ],
            output='screen'
        ),

        # ▶ Lanza RViz con configuración específica (si tienes)
        ExecuteProcess(
            cmd=['rviz2', '-d', rviz_config_path],
            output='screen'
        ),

        # ▶ Lanza RQT
        ExecuteProcess(
            cmd=['rqt'],
            output='screen'
        ),

        # ▶ Nodo de control del brazo (si lo tienes)
        Node(
            package='rincon_charris_pkg',
            executable='controlador_brazo',
            name='controlador_brazo_node',
            output='screen'
        )
    ])

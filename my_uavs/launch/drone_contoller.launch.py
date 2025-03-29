import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction

def generate_launch_description():
    return LaunchDescription([
        # Spawn drone r1 (Starts immediately)
        Node(
            package='my_uavs',
            executable='drone_controller_d1.py',
            name='r1_controller',
            output='screen',
            arguments=['r1']
        ),

        # Spawn drone r2 with a delay of 3 seconds
        TimerAction(
            period=2.3,  # Delay before launching r2
            actions=[
                Node(
                    package='my_uavs',
                    executable='drone_controller_d1.py',
                    name='r2_controller',
                    output='screen',
                    arguments=['r2']
                ),
            ],
        ),

    ])


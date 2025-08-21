from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[{
                # General settings
                'use_sim_time': False,
                'frequency': 30.0,
                'sensor_timeout': 0.1,
                'two_d_mode': True,
                'publish_tf': True,

                # Frame definitions
                'map_frame': 'map',
                'odom_frame': 'odom',
                'base_link_frame': 'base_footprint',
                'world_frame': 'odom',

                # Odom input (from base_node_X3)
                'odom0': '/odom_raw',
                'odom0_config': [
                    True,  True,  False,   # x, y, z
                    False, False, True,    # roll, pitch, yaw
                    False, False, False,   # vx, vy, vz
                    False, False, False,   # vroll, vpitch, vyaw
                    False, False, False    # ax, ay, az
                ],
                'odom0_differential': False,
                'odom0_relative': False,

                # IMU input (from imu_filter_madgwick)
                'imu0': '/imu/data',
                'imu0_config': [
                    False, False, False,   # x, y, z
                    True,  True,  True,    # roll, pitch, yaw
                    False, False, False,   # vx, vy, vz
                    True,  True,  True,    # vroll, vpitch, vyaw
                    False, False, False    # ax, ay, az
                ],
                'imu0_differential': False,
                'imu0_relative': False
            }]
        )

    ])

import os
import xacro
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Package Directory
    pkg_rosbot = get_package_share_directory('rosbot_description')

    # Parse robot description from xacro
    robot_description_file = os.path.join(pkg_rosbot, 'urdf', 'new.xacro')
    robot_description_config = xacro.process_file(robot_description_file)
    robot_description = {'robot_description': robot_description_config.toxml()}

    # Robot State Publisher (use_sim_time should be false on real robot)
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[robot_description, {'use_sim_time': False}],
    )

    return LaunchDescription([
        robot_state_publisher
    ])


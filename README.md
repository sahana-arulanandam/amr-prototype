Order of commands executed:

ros2 launch yahboomcar_bringup yahboomcar_bringup_X3_launch.py
ros2 launch rplidar_ros rplidar_c1_launch.py 
ros2 launch rosbot_description state-publisher.launch.py
ros2 launch rosbot_nav2_bringup slam_online_async.launch.py

ros2 run joy joy_node
ros2 launch joystick_node joystick_node_launch.launch.py 
rviz2

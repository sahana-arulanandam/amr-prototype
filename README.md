Order of commands executed:

1. ros2 launch yahboomcar_bringup yahboomcar_bringup_X3_launch.py
2. ros2 launch rplidar_ros rplidar_c1_launch.py 
3. ros2 launch rosbot_description state-publisher.launch.py
4. ros2 launch rosbot_nav2_bringup slam_online_async.launch.py

5. ros2 run joy joy_node
6. ros2 launch joystick_node joystick_node_launch.launch.py 
7. rviz2

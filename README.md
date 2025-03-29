**drone_collision_avoiding--ROS2**

OS: UBUNTU 22.04

ROS DISTRO: HUMBLE


To launch One drone in gazebo:

In terminal 1:

         ros2 launch my_uavs ign_world_launch.py 

Output:

![image](https://github.com/user-attachments/assets/67127f5e-ae36-45a0-a94f-1b252942df5e)

In terminal 2:
Run the ros2 node to run the waypoints for the primary drone:

    ros2 run my_uavs drone_controller_d1.py 

This node: takes off the r1 drone, goes forward and then lands.

Now to launch the collision avoidance:

In terminal 1: launch 2 drones in gazebo ignition.

      ros2 launch my_uavs two_ign_world_launch.py 

![image](https://github.com/user-attachments/assets/689f7ece-9369-433a-8273-d3a6deb29113)

In terminal 2: launch collision_predictor node:

      ros2 run my_uavs collision_predictor.py 

This runs the collision avoiderlogic, now to test this I have made two test cases:

In case-1: The both drones doesn't collide.
In terminal 3:

    ros2 launch my_uavs safe_drone_launch.py 

Case-2:

    ros2 launch my_uavs drone_contoller.launch.py 
When both the drones collide, our algo detects the proximity of both the drones and then when it crosses then threshold. Drone 2 lands:

  
  ![image](https://github.com/user-attachments/assets/d0270219-dcf4-4b3d-9002-eee98a82aa6e)


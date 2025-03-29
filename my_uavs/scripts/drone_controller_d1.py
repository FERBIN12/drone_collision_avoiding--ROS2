#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import time

class DroneController(Node):
    def __init__(self, drone_name):
        super().__init__(f'{drone_name}_controller')
        self.cmd_vel_publisher = self.create_publisher(Twist, f'/{drone_name}/cmd_vel', 10)
        self.drone_name = drone_name
        self.get_logger().info(f"{drone_name} Controller Node Started")

    def move_drone(self):
        takeoff_msg = Twist()
        takeoff_msg.linear.z = 1.0  # Ascend
        
        forward_msg = Twist()
        forward_msg.linear.x = 1.0  # Move forward
        
        land_msg = Twist()
        land_msg.linear.z = -1.0  # Descend
        
        stop_msg = Twist()  # Stop motion
        
        # Takeoff
        self.get_logger().info(f"{self.drone_name} Taking off")
        self.cmd_vel_publisher.publish(takeoff_msg)
        time.sleep(4)
        
        # Move forward
        self.get_logger().info(f"{self.drone_name} Moving forward")
        self.cmd_vel_publisher.publish(forward_msg)
        time.sleep(12)
        
        # Land
        self.get_logger().info(f"{self.drone_name} Landing")
        self.cmd_vel_publisher.publish(land_msg)
        time.sleep(4)
        
        # Stop motion
        self.get_logger().info(f"{self.drone_name} Stopping")
        self.cmd_vel_publisher.publish(stop_msg)

def main(args=None):
    rclpy.init(args=args)

    if len(sys.argv) < 2:
        print("Usage: ros2 run my_uavs controller.py <drone_name>")
        return

    drone_name = sys.argv[1]
    controller = DroneController(drone_name)
    controller.move_drone()
    controller.destroy_node()
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()

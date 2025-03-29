#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
import math

class CollisionPredictor(Node):
    def __init__(self):
        super().__init__('collision_predictor')

        # Subscribe to odometry topics for both drones
        self.odom_sub_r1 = self.create_subscription(Odometry, '/r1/odom', self.odom_callback_r1, 10)
        self.odom_sub_r2 = self.create_subscription(Odometry, '/r2/odom', self.odom_callback_r2, 10)

        # Publisher to control r2 (descending command)
        self.r2_cmd_vel_publisher = self.create_publisher(Twist, '/r2/cmd_vel', 10)

        # Store positions
        self.r1_position = None
        self.r2_position = None

        # Collision threshold (meters)
        self.collision_threshold = 0.5  # Adjust as needed

        self.get_logger().info("Collision Predictor Node Started")

    def odom_callback_r1(self, msg):
        """Callback function for r1 odometry"""
        self.r1_position = (msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z)
        self.check_collision()

    def odom_callback_r2(self, msg):
        """Callback function for r2 odometry"""
        self.r2_position = (msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z)
        self.check_collision()

    def check_collision(self):
        """Check if r1 and r2 will collide, and descend r2 if needed"""
        if self.r1_position and self.r2_position:
            distance_xy = math.dist(self.r1_position[:2], self.r2_position[:2])
            
            if distance_xy < self.collision_threshold:
                self.get_logger().warn(
                    f"🚨 WARNING: Possible collision! r1 and r2 are {distance_xy:.2f}m apart. Lowering r2."
                )
                self.descend_r2()

    def descend_r2(self):
        """Command r2 to descend"""
        descend_msg = Twist()
        descend_msg.linear.z = -0.5  # Descend speed

        self.r2_cmd_vel_publisher.publish(descend_msg)

        self.get_logger().info("🔽 r2 is descending to avoid collision.")

def main(args=None):
    rclpy.init(args=args)
    node = CollisionPredictor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

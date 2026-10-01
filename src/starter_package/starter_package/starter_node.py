#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

class Starter_Node(Node):

    def __init__(self)->None:
        super().__init__("starter_node")

        self.velocity_publisher = self.create_publisher(
            Twist,
            "/cmd_vel",
            10,
        )

    def create_velocity_msg(self, angular_vel:float) -> None:
        msg = Twist()

        msg.linear.x = 0.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0

        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = angular_vel

        self.velocity_publisher.publish(msg)

def main(args=None)->None:
    rclpy.init(args=args)

    starter_node = Starter_Node()

    try:
        rclpy.spin(starter_node)
    except KeyboardInterrupt:
        pass
    finally:
        if starter_node: starter_node.destroy_node()

    rclpy.shutdown()

if __name__ == "__main__":
    main()
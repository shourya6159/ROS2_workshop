#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

class Velocity_Publisher(Node):

    def __init__(self)->None:
        super().__init__("velocity_publisher")

        self.publisher = self.create_publisher(
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

        self.publisher.publish(msg)

def main(args=None)->None:
    rclpy.init(args=args)

    velocity_publisher = Velocity_Publisher()

    try:
        rclpy.spin(velocity_publisher)
    except KeyboardInterrupt:
        pass
    finally:
        if velocity_publisher: velocity_publisher.destroy_node()

    rclpy.shutdown()

if __name__ == "__main__":
    main()

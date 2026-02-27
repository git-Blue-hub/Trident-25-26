# A simple ROS2 Publisher

import rclpy 
from rclpy.node import Node

from geometry_msgs.msg import TwistStamped

class Moving(Node):
    
    def __init__(self):
        super().__init__("Moving")

        self.my_publisher = self.create_publisher(
        msg_type=TwistStamped, 
        topic="/cmd_vel", 
        qos_profile=10, 
        )

        publish_rate = 10 # Hz
        self.timer = self.create_timer(
        timer_period_sec=1/publish_rate, 
        callback=self.timer_callback
        )

        self.get_logger().info(f"The '{self.get_name()}' node is initialised." )

    
    def timer_callback(self):
        radius = 0.5 # meters
        linear_velocity = 0.1 # meters per second [m/s]

        topic_msg = TwistStamped() 
        topic_msg.twist.linear.x = linear_velocity

        self.my_publisher.publish(topic_msg) 

        self.get_logger().info( 
            f"Linear Velocity: {topic_msg.twist.linear.x:.2f} [m/s], ",
            throttle_duration_sec=1, 
        )

def main(args=None): 
    rclpy.init(args=args)
    movement = Moving()
    rclpy.spin(movement)
    movement.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':  
    main()
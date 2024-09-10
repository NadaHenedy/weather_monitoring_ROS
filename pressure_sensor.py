#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String , Float32
import random
from temperature_sensor.msg import PressureSensor

class pressure(Node):
     def __init__(self):
        super().__init__("pressure")
        self.pressure = self.create_publisher(PressureSensor , "pressure", 10)
        self.timer_ = self.create_timer(2 , self.pressure_read)
        self.node_status = "OK"
        self.get_logger().info("pressure node started")
    
     def pressure_read(self):
        try:
            press = random.uniform(0.95,1.2)
        except Exception as e:
            self.node_status = "Error:"+str(e)
            self.get_logger().info(f" Error reading pressure:{e}")
            return 
        pressure_msg = PressureSensor()
        pressure_msg.pressure = press
        pressure_msg.node_status = self.node_status
        self.pressure.publish(pressure_msg)


def main(args=None):
    rclpy.init(args=args)
    node = pressure()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()

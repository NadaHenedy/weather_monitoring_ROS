#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String , Float32
import random
from temperature_sensor.msg import TemperatureSensor

class temperature(Node):
     def __init__(self):
        super().__init__("temperature")
        self.temperature = self.create_publisher(TemperatureSensor , "temperature", 10)
        self.timer_ = self.create_timer(2 , self.temperature_read)
        self.node_status = "OK"
        self.get_logger().info("temperature node started")
    
     def temperature_read(self):
        try:
            temp = random.uniform(10,100)
        except Exception as e:
            self.node_status = "Error:"+str(e)
            self.get_logger().info(f" Error reading temperature:{e}")
            return 
        temp_msg = TemperatureSensor()
        temp_msg.temperature = temp
        temp_msg.node_status = self.node_status
        self.temperature.publish(temp_msg)


def main(args=None):
    rclpy.init(args=args)
    node = temperature()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String , Float32
import random
from temperature_sensor.msg import TemperatureSensor

class humidity(Node):
     def __init__(self):
        super().__init__("temperature")
        self.humidity = self.create_publisher(TemperatureSensor , "humidity", 10)
        self.timer_ = self.create_timer(2 , self.humidity_read)
        self.node_status = "OK"
        self.get_logger().info("humidity node started")
    
     def humidity_read(self):
        try:
            humd = random.uniform(0.95,1.2)
        except Exception as e:
            self.node_status = "Error:"+str(e)
            self.get_logger().info(f" Error reading humidity:{e}")
            return 
        hum_msg = TemperatureSensor()
        hum_msg.humidity = humd
        hum_msg.node_status = self.node_status
        self.humidity.publish(hum_msg)


def main(args=None):
    rclpy.init(args=args)
    node = humidity()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()

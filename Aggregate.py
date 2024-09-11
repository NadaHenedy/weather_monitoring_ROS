#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String , Float32
import random
from temperature_sensor.msg import TemperatureSensor
from temperature_sensor.msg import HumiditySensor
from temperature_sensor.msg import PressureSensor
from temperature_sensor.msg import AggregateData


class Aggregation(Node):
     def __init__(self):
        super().__init__("aggregate")
        self.subtemperature = self.create_subscription(TemperatureSensor,"temperature",self.callback_tempertaure,10)
        self.subhumidity = self.create_subscription(HumiditySensor , "humidity", self.callback_humidity,10)
        self.subpressure = self.create_subscription(PressureSensor,"pressure",self.callback_pressure,10)

        self.aggregate = self.create_publisher(AggregateData,"aggregate",10)

        self.get_logger().info("aggregate node started")

        self.data={}

     def callback_tempertaure(self,msg:TemperatureSensor):
        self.data["temperature"] = msg.temperature
        self.data["node_status_temp"] = msg.node_status
        self.check()

     def callback_humidity(self,msg:HumiditySensor):
        self.data["humidity"] = msg.humidity
        self.data["node_status_hum"] = msg.node_status

        self.check()

     def callback_pressure(self,msg:PressureSensor):
        self.data["pressure"] = msg.pressure
        self.data["node_status_press"] = msg.node_status

        self.check()

     def check(self):
        if all(key in self.data for key in ["temperature" , "humidity" , "pressure"]):
            agg_msg = AggregateData()
            agg_msg.temperature = self.data["temperature"]
            agg_msg.humidity = self.data["humidity"]
            agg_msg.pressure = self.data["pressure"]
            agg_msg.node_status_temperature = self.data["node_status_temp"]
            agg_msg.node_status_humidity = self.data["node_status_hum"]
            agg_msg.node_status_pressure = self.data["node_status_press"]

            self.aggregate.publish(agg_msg)
            self.data = {}

def main(args=None):
    rclpy.init(args=args)
    node = Aggregation()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()

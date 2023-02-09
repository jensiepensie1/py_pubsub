import serial

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('_')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        ser.reset_input_buffer()
        while True:
            if ser.in_waiting > 0:
                msg = String()
                msg.data = ser.readline().decode('utf-8').rstrip()
                self.publisher_.publish(msg)
                self.get_logger().info('Publishing: "%s"' % msg.data)


    def timer_callback(self):
        msg = String()
        msg.data = ser.readline().decode('utf-8').rstrip()
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    
    
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':

    main()

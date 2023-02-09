import serial

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class BatterijSpanningPublisher(Node):

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



def main(args=None):
    
    
    rclpy.init(args=args)

    Batterij_Spanning_Publisher = BatterijSpanningPublisher()

    rclpy.spin(Batterij_Spanning_Publisher)

    Batterij_Spanning_Publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':

    main()
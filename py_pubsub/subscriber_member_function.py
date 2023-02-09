import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class BatterijSpanningSubscriber(Node):

    def __init__(self):
        super().__init__('_')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info(msg.data)


def main(args=None):
    rclpy.init(args=args)

    Batterij_Spanning_Subscriber = BatterijSpanningSubscriber()

    rclpy.spin(Batterij_Spanning_Subscriber)

    Batterij_Spanning_Subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

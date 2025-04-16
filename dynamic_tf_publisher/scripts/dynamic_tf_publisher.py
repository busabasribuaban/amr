import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
import tf2_ros
from math import radians
import time

class DynamicTFPublisher(Node):
    def __init__(self):
        super().__init__('dynamic_tf_publisher')
        self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.broadcast_dynamic_tf)  # Broadcast every 0.1 seconds

    def broadcast_dynamic_tf(self):
        t = TransformStamped()

        # Setup the transform
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'base_link'  # Base frame
        t.child_frame_id = 'laser'  # Child frame (laser sensor)

        # Set translation (e.g., robot base to laser position)
        t.transform.translation.x = 1.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0

        # Set rotation (for dynamic rotation, you can update the rotation here)
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        # Broadcast the transform
        self.tf_broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = DynamicTFPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

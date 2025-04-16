import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from sensor_msgs.msg import Imu
import tf2_ros
from math import radians
import tf2_geometry_msgs

class DynamicTFPublisher(Node):
    def __init__(self):
        super().__init__('dynamic_tf_publisher')
        self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.broadcast_dynamic_tf)  # Broadcast every 0.1 seconds
        
        # Subscribe to IMU data
        self.imu_subscription = self.create_subscription(
            Imu,
            '/imu/data',  # Topic ของ IMU, ปรับให้ตรงกับที่คุณใช้
            self.imu_callback,
            10
        )

        # Initialize rotation quaternion
        self.current_rotation = [0.0, 0.0, 0.0, 1.0]  # Default quaternion (identity rotation)

    def imu_callback(self, msg):
        # ใช้ข้อมูลจาก IMU เพื่ออัพเดตการหมุน (rotation)
        self.current_rotation = [msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w]

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

        # Set rotation based on IMU data (use quaternion from IMU)
        t.transform.rotation.x = self.current_rotation[0]
        t.transform.rotation.y = self.current_rotation[1]
        t.transform.rotation.z = self.current_rotation[2]
        t.transform.rotation.w = self.current_rotation[3]

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



from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    enable_slam = LaunchConfiguration('enable_slam')

    declare_use_sim_time = DeclareLaunchArgument(
        'use_sim_time', default_value='false',
        description='Use simulation time if true'
    )

    declare_enable_slam = DeclareLaunchArgument(
        'enable_slam', default_value='true',
        description='Launch SLAM Toolbox if true'
    )

    ekf_config_path = os.path.join(
        get_package_share_directory('my_robot_localization'),
        'config',
        'ekf.yaml'
    )

    slam_config_path = os.path.join(
        get_package_share_directory('my_robot_localization'),
        'config',
        'slam_toolbox.yaml'
    )

    ekf_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_localization_node',
        output='screen',
        parameters=[ekf_config_path, {'use_sim_time': use_sim_time}]
    )

    slam_node = Node(
        package='slam_toolbox',
        executable='sync_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[slam_config_path, {'use_sim_time': use_sim_time}],
        condition=IfCondition(enable_slam)
    )

    ld = LaunchDescription()
    ld.add_action(declare_use_sim_time)
    ld.add_action(declare_enable_slam)
    ld.add_action(ekf_node)
    ld.add_action(slam_node)

    return ld


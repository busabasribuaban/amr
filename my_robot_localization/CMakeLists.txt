cmake_minimum_required(VERSION 3.8)
project(my_robot_localization)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(robot_localization REQUIRED)

install(DIRECTORY launch config
  DESTINATION share/${PROJECT_NAME}
)

ament_package()

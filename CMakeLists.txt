cmake_minimum_required(VERSION 3.5)
project(mask_rcnn)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
#find_package(rclpy REQUIRED)
#find_package(std_msgs REQUIRED)
#find_package(sensor_msgs REQUIRED)

ament_package()

install(PROGRAMS
  samples/balloon/balloon.py
  DESTINATION lib/${PROJECT_NAME}
)

install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

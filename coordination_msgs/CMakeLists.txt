cmake_minimum_required(VERSION 3.0.2)
project(coordination_msgs)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  message_generation
  std_msgs
)

add_message_files(
 FILES
 InitialCoordination.msg
)

generate_messages(
 DEPENDENCIES
 std_msgs
)
catkin_package(
  CATKIN_DEPENDS
  message_runtime
  std_msgs
)

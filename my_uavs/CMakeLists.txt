cmake_minimum_required(VERSION 3.5)
project(my_uavs)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)

install(DIRECTORY
  launch urdf rviz src scripts models worlds
  DESTINATION share/${PROJECT_NAME})


# Install Python modules
ament_python_install_package(${PROJECT_NAME}) #It is required the __init__.py inside the PROJECT_NAME folder

# Install Python executables #They must start with the shebag tag and must have execution permision
install(PROGRAMS
  scripts/drone_controller_d1.py
  scripts/collision_predictor.py
  
  DESTINATION lib/${PROJECT_NAME} )

ament_package()



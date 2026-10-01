# ROS 2 Workspace Setup Guide

This guide outlines the standard sequence of commands to create a ROS 2 workspace, build it, and generate your first Python package. 

## 1. Navigate to the Workspace
Rename the extracted directory to ROS2_workshop
Then run:
```bash
cd ~/ROS2_workshop
```

## 2. Initial Build
Even though the workspace is empty, it's good practice to build it once to generate the standard `build`, `install`, and `log` directories.
```bash
colcon build
```

## 3. Source the Workspace
After building, source your new workspace's overlay so your terminal recognizes it.
```bash
source install/setup.bash
```

## 4. Create a New Package
Navigate into the `src` directory to create new packages. Here, we create a Python package named `my_py_pkg` with a dependency on `rclpy`.
```bash
cd ~/ROS2_workshop/src
ros2 pkg create --build-type ament_python my_py_pkg --dependencies rclpy
```

## 5. Build the New Package
Go back to the root of your workspace to build. You can build the entire workspace with `colcon build`, or build just your specific package using the `--packages-select` flag.
```bash
cd ~/ROS2_workshop
colcon build
```

## 6. Source the Updated Workspace
Whenever you build new packages or executables, you must source the workspace again so ROS 2 can find them.
```bash
source install/setup.bash
```

## 7. Run the launch file
```bash
ros2 launch starter_package system_bringup.launch.py
```

## 8. Create new terminal


## 9. Run the teleop keyboard:
```bash
source /opt/ros/humble/setup.bash
sudo apt install ros-humble-teleop-twist-keyboard
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

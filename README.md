# ROS 2 Workspace Setup Guide

This guide outlines the standard sequence of commands to create a ROS 2 workspace, build it, and generate your first Python package. 

## 1. Navigate to the Workspace
Rename the extracted directory to ROS2_workshop
Then run:
```bash
cd ~/ROS2_workshop
```
## 2. Build workspace
```bash
colcon build
```

## 3. Source the Workspace
Whenever you build new packages or executables, you must source the workspace so ROS 2 can find them.
```bash
source install/setup.bash
```

## 4. Run the launch file
```bash
ros2 launch starter_package system_bringup.launch.py
```

## 5. Create new terminal


## 6. Run the teleop keyboard:
```bash
source /opt/ros/humble/setup.bash
sudo apt install ros-humble-teleop-twist-keyboard
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
## PHASE 2
## OPEN CV
Open a new terminal and:
## 1. Install required dependencies
```bash
sudo apt update
sudo apt install ros-humble-cv-bridge python3-opencv
```

## 2. Install Pyzbar
```bash
sudo apt install libzbar0 python3-pyzbar
```
## 3. Run the QR scanner script
```bash
source /opt/ros/humble/setup.bash
cd ~/ROS2_workshop
python3 qr_scanner.py
```

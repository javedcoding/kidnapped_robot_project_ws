# kidnapped_robot_project_ws
This is a project for solving kidnapped robot problem using computer vision using RPLIDAR and Intel Realsense D435 depth camera.
#Installation
First we need to install ROS. the compatibility of ROS OS and Nvidia graphics card is cumbersome. So we chose Ubuntu 20.04 (focal fossa), ros noetic, Cuda dnn 11.8, Cuda 515, tensorRT 8.5.3
To install ros do these commands available in roswiki. Before progressing turn on software updater's Source code and Canonical Partners download option
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt install curl # if you haven't already installed curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo apt update
sudo apt install ros-noetic-desktop-full
sudo apt install ros-noetic-slam-gmapping
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
sudo apt install python3-rosdep
sudo rosdep init
rosdep update
```
To download turtlebot3 follow these commands from emanual.robotis.com
```
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy \
  ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc \
  ros-noetic-rgbd-launch ros-noetic-depthimage-to-laserscan \
  ros-noetic-rosserial-arduino ros-noetic-rosserial-python \
  ros-noetic-rosserial-server ros-noetic-rosserial-client \
  ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server \
  ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
  ros-noetic-compressed-image-transport ros-noetic-rqt* \
  ros-noetic-gmapping ros-noetic-navigation ros-noetic-interactive-markers
$ sudo apt-get install ros-noetic-dynamixel-sdk
$ sudo apt-get install ros-noetic-turtlebot3-msgs
$ sudo apt-get install ros-noetic-turtlebot3
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
```
To install cuda search for the cuda toolkit of that version
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget http://developer.download.nvidia.com/compute/cuda/11.0.2/local_installers/cuda-repo-ubuntu2004-11-0-local_11.0.2-450.51.05-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2004-11-0-local_11.0.2-450.51.05-1_amd64.deb
sudo apt-key add /var/cuda-repo-ubuntu2004-11-0-local/7fa2af80.pub
sudo apt-get update
sudo apt-get -y install cuda
```
Check tensorflow compatibility with cuda driver here https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html
Download corresponding cudnn file also from Nvidia account
Now install tensorRT
```
sudo apt-get install tensorrt
sudo apt-get install libnvinfer-lean8
sudo apt-get install libnvinfer-vc-plugin8
sudo apt-get install python3-libnvinfer-lean
sudo apt-get install python3-libnvinfer-dispatch
python3 -m pip install numpy
sudo apt-get install python3-libnvinfer-dev
python3-libnvinfer
python3-libnvinfer-lean
python3-libnvinfer-dispatch
python3 -m pip install protobuf
sudo apt-get install uff-converter-tf
python3 -m pip install numpy onnx
sudo apt-get install onnx-graphsurgeon
dpkg-query -W tensorrt
```
Now download this repository and create a workspace folder to run these code
```
mkdir catkin_ws
cd catkin_ws
mkdir src
cd ..
catkin build
cd src
```
After downloading this repository file inside the workspace download corresponding srdf model from the link below into /pr2/pr2_tc_gazebo/models/ folder:
https://drive.google.com/drive/folders/1jw35blIMJ4rWBSyOFR4qXUlZ1oZoBsPh?usp=share_link
Run the project using these commands:
```
roslaunch pr2_tc_gazebo main_standing_detection.launch
roslaunch room_detection_pkg dark_net_3d.launch
rosrun room_detection_pkg detector.py
rosrun init_pose
rosrun goal_pose
```
Other related turtlebot3 simulation launch run you can find in this link:
https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/

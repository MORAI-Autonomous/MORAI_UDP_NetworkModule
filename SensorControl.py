from lib.network.UDP import Sender
from lib.define.SensorControl import SensorControl

IP = '127.0.0.1' 
PORT = 9103

#Protocol 정보 
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/ros-1#id-(24.R2-ko)통신메시지프로토콜-SensorControl
def main():
    sensorcontrol = Sender(IP, PORT)

    data = SensorControl()
    data.sensorIndex = 1
    data.pose_x = 3.2
    data.pose_y = 0.0
    data.pose_z = 0.6
    data.roll = 0.0
    data.pitch = 0.0
    data.yaw = 0.0
    
    sensorcontrol.send(data)


if __name__ == '__main__':
    main()
import time
from lib.network.UDP import Receiver
from lib.define.IMU import IMU

IP = '127.0.0.1' 
PORT = 1111

#Protocol 정보
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/ros-1#id-(24.R2-ko)통신메시지프로토콜-EgoVehicleStatus.1

import ctypes
print(ctypes.sizeof(IMU()))
def main():
    sensor_imu = Receiver(IP, PORT, IMU())
    while True :
        imu_data = sensor_imu.get_data()
        print(imu_data)
        
        time.sleep(0.1)

if __name__ == '__main__':
    main()
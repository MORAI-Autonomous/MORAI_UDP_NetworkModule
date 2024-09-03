import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import time
from lib.network.UDP import Receiver
from lib.define.EgoVehicleStatus import EgoVehicleStatus

IP = '127.0.0.1' 
PORT = 909

#Protocol 정보
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/ros-1#id-(24.R2-ko)통신메시지프로토콜-EgoVehicleStatus.1
def main():
    egovehiclestatus = Receiver(IP, PORT, EgoVehicleStatus())
    while True :
        status = egovehiclestatus.get_data()
        print(status)        
        time.sleep(0.1)
        
if __name__ == '__main__':
    main()
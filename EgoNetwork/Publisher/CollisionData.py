import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import time
from lib.network.UDP import Receiver
from lib.define.CollisionData import CollisionData

IP = '127.0.0.1' 
PORT = 9092

#Protocol 정보
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/ros-1#id-(24.R2-ko)통신메시지프로토콜-CollisionData.1

def main():
    coliisiondata = Receiver(IP, PORT, CollisionData())
    while True :
        status = coliisiondata.get_data()        
        print(status)
        time.sleep(0.1)

if __name__ == '__main__':
    main()
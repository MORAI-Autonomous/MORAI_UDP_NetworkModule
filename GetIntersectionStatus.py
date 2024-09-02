import time
from lib.network.UDP import Receiver
from lib.define.GetIntersectionStatus import GetIntersectionStatus

IP = '127.0.0.1' 
PORT = 9102

#Protocol정보
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/ros-1#id-(24.R2-ko)통신메시지프로토콜-GetIntersectionStatus.1
def main():
    intersectionStatus = Receiver(IP, PORT, GetIntersectionStatus())
    while True :
        status = intersectionStatus.get_data()        
        print(status)        
        time.sleep(0.1)

if __name__ == '__main__':
    main()
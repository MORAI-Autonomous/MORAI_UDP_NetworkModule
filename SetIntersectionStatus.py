from lib.network.UDP import Sender
from lib.define.SetIntersectionStatus import SetIntersectionStatus

IP = '127.0.0.1' 
PORT = 9132

#Protocol 정보 
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/ros-1#id-(24.R2-ko)통신메시지프로토콜-SetIntersectionStatus

#교차로 제어 정보 
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/-17
def main():
    set_intersection = Sender(IP, PORT)

    data = SetIntersectionStatus()    
    data.IntIndex = 5
    data.IntStatus = 0
    data.IntTime = 0 
    
    set_intersection.send(data)


if __name__ == '__main__':
    main()
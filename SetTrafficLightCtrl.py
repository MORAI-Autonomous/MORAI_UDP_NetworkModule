from lib.network.UDP import Sender
from lib.define.SetTrafficLightCtrl import SetTrafficLightCtrl

IP = '127.0.0.1' 
PORT = 7607

#Protocol정보
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/ros-1#id-(24.R2-ko)통신메시지프로토콜-SetIntersectionStatus
def main():
    set_traffic = Sender(IP, PORT)

    data = SetTrafficLightCtrl()    
    data.trafficLightIndex = "C119BS010025".encode() 
    data.trafficLightStatus = 1
    ''' Status Info 
    Red : 1
    Yellow : 4
    Green : 16
    GreenLeft : 32
    Green with GreenLeft : 48
    Yellow with Green : 20
    Yellow with GreenLeft : 36
    Red with Yellow: 5
    default : -1   
    '''

    set_traffic.send(data)



if __name__ == '__main__':
    main()
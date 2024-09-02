from lib.network.UDP import Sender
from lib.define.MultiEgoSetting import MultiEgoSetting

IP = '127.0.0.1' 
PORT = 7604

#Protocol정보
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/ros-1#id-(24.R2-ko)통신메시지프로토콜-MultiEgoSetting.1
"""
MuleiEgoSEtting을 사용하기 위해서 Network setting > Simulator network > Connect 해야함
"""
def main():
    multi_ego_setting = Sender(IP, PORT)

    multi_ego = MultiEgoSetting()    
    multi_ego.Num_of_Ego = 1
    multi_ego.Cam_index = 0

    multi_ego.data[0].ego_index = 0 
    multi_ego.data[0].position_x = 26.43
    multi_ego.data[0].position_y = 1115.30
    multi_ego.data[0].position_z = -0.39
    multi_ego.data[0].roll = 0.878
    multi_ego.data[0].pitch = 1.525
    multi_ego.data[0].yaw = 3.831
    multi_ego.data[0].velocity = 0 #km/h
    multi_ego.data[0].gear = 1 # 1: Parking    2: Rear    3: Neutral   4:Drive    
    multi_ego.data[0].ctrl_mode = 1 # 1: Keyboard   2:Automode
    
    multi_ego_setting.send(multi_ego) 

if __name__ == '__main__':
    main()
import time
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from lib.network.UDP import Sender
from lib.define.EgoCtrlCmd import EgoCtrlCmd

IP = '127.0.0.1' 
PORT = 9093

#Protocol정보
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/ros-1#id-(24.R2-ko)통신메시지프로토콜-EgoCtrlCmd.1
"""
Ego Ghost Mode를 사용하기 위해서 Network setting > Cmd Control을 MoraiGhostCmdController로 Connect 해야함
'Q' 를 눌러 Ego Controller를 AV- ExternalCtrl로 설정 해야 동작함.
아래 예제는 특정 주차공간에 Ego 차량을 Ghost Mode로 위치 시켰지만
Log 파일이나, 다른 실시간 데이터를 받아 위치/자세 값을 반복적으로 송신하면 차량이 주행하는 것처럼 보임.
"""
def main():
    ego_ctrl = Sender(IP, PORT)

    data = EgoCtrlCmd()    
    import ctypes 
    print(ctypes.sizeof(EgoCtrlCmd()))

    data.ctrl_mode = 2 # 1 : Keyboard   2 : AutoMode
    data.gear = 4  
    """
    index   0   1   2   3   4   5
    Gear    M   P   R   N   D   L
    """
    
    """
    1: Throttle(accel,brake,steer) 
    2: Velocity(velocity,steer)
    3: Acceleration(acceleration,steer)
    """
    data.cmd_type = 1
    data.accel = 0.5
    data.brake = 0.1

    # data.cmd_type = 2
    # data.velocity = 30 #km

    # data.cmd_type = 3
    # data.acceleration = 5 #m/s2
    
    data.steer = 0.1 # -1 ~ 1  
    while 1:
        ego_ctrl.send(data)
        time.sleep(0.1)

        

if __name__ == '__main__':
    main()
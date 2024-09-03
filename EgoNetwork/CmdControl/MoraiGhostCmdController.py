import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from lib.network.UDP import Sender
from lib.define.EgoGhostCtrlCmd import EgoGhostCtrlCmd

IP = '127.0.0.1' 
PORT = 9095

#Protocol정보
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/ego-ghost-mode#id-(24.R2-ko)EgoGhostMode사용방법-GhostCtrlCmd.1
"""
Ego Ghost Mode를 사용하기 위해서 Network setting > Cmd Control을 MoraiGhostCmdController로 Connect 해야함
'Q' 를 눌러 Ego Controller를 AV- ExternalCtrl로 설정 해야 동작함.
아래 예제는 특정 주차공간에 Ego 차량을 Ghost Mode로 위치 시켰지만
Log 파일이나, 다른 실시간 데이터를 받아 위치/자세 값을 반복적으로 송신하면 차량이 주행하는 것처럼 보임.
"""
def main():
    ego_ghost = Sender(IP, PORT)

    data = EgoGhostCtrlCmd()    

    data.pose_x = 26.43
    data.pose_y = 1115.30
    data.pose_z = -0.39
    data.roll = 0.878
    data.pitch = 1.525
    data.yaw = 3.831
    data.velocity = 0
    data.steer = 0

    ego_ghost.send(data)

if __name__ == '__main__':
    main()
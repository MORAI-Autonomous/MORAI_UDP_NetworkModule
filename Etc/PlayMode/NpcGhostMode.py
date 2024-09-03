import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from lib.network.UDP import Sender
from lib.define.NpcGhostMode import NpcGhostMode

IP = '127.0.0.1' 
PORT = 9101

#Protocol정보
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/npc-ghost-mode#id-(24.R2-ko)NPCGhostMode사용방법-NPCGhostController.1
"""
Npc Ghost Mode를 사용하기 위해서 PlayMode > Ghost > Npc Ghost Mode를 Connect해야 한다.
Connect 버튼을 눌렀을 때 Disconnect 버튼이 표시되지않는다면 연결이 제대로 되지않아
Port 번호를 확인해야 한다(Network setting과 중복체크)

아래 예제는 특정 주차공간에 Npc 차량을 Ghost Mode로 위치 시켰지만
Log 파일이나, 다른 실시간 데이터를 받아 위치/자세 값을 반복적으로 송신하면 차량이 주행하는 것처럼 보임.
"""
def main():
    npc_ghost = Sender(IP, PORT)

    data = NpcGhostMode()    
    data.data[0].unique_id = 3
    data.data[0].car_name = '2015_Kia_K5'.ljust(25).encode()
    data.data[0].pose_x = 25.07
    data.data[0].pose_y = 1112.75
    data.data[0].pose_z = -0.39
    data.data[0].roll = 0.878
    data.data[0].pitch = 1.525
    data.data[0].yaw = 3.144


    npc_ghost.send(data)

if __name__ == '__main__':
    main()
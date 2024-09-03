import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from lib.network.UDP import Sender
from lib.define.ScenarioLoad import SetScenarioLoad

IP = '127.0.0.1' 
PORT = 9099

#Protocol 정보 
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/ros-1#id-(24.R2-ko)통신메시지프로토콜-ScenarioLoad.1
def main():
    set_scenario = Sender(IP, PORT)

    data = SetScenarioLoad()                
    data.filename = 'lattice'.ljust(30).encode()    
    data.delete_all = False
    data.network = False
    data.ego = True
    data.npc = True
    data.pedestrian = True
    data.object = True
    data.pause = True

    set_scenario.send(data)


if __name__ == '__main__':
    main()
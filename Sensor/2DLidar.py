import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from lib.network.UDP import Receiver
from lib.define.Lidar_2D import MORAILIDAR, LIDAR_UTILS

IP = '127.0.0.1' 
PORT = 1111

#Protocol 정보
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/-35#id-(24.R2-ko)센서통신프로토콜-2DLiDAR

def main():    
    lidar_data = Receiver(IP, PORT, MORAILIDAR())    
    
    utils = LIDAR_UTILS()
    utils.setData(lidar_data)
    utils.visualization()
    
if __name__ == '__main__':
    main()
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from lib.network.UDP import Sender
from lib.define.SaveSensorData import SaveSensorData

IP = '127.0.0.1' 
PORT = 9105

#Protocol 정보 
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/ros-1#id-(24.R2-ko)통신메시지프로토콜-SaveSensorData.1
def main():
    savesensordata = Sender(IP, PORT)

    data = SaveSensorData()
    data.custom = False
    data.file_name = 'test'.ljust(30).encode()  
    data.file_dir = 'C:\\'.ljust(60).encode()

    savesensordata.send(data)


if __name__ == '__main__':
    main()
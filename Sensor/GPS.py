import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import time
from lib.network.UDP import Receiver
from lib.define.GPS import GPS

IP = '127.0.0.1' 
PORT = 1111

#Protocol 정보
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/ros-1#id-(24.R2-ko)통신메시지프로토콜-EgoVehicleStatus.1

def main():
    sensor_gps = Receiver(IP, PORT, GPS())
    while True :
        gps_data = sensor_gps.get_data()
        gps_data.parsing()
        
        print(f'GPRMC | lat : {gps_data.gprmc.lat:.6f} \t lon : {gps_data.gprmc.lon:.6f}')
        print(f'GPGGA | lat : {gps_data.gpgga.lat:.6f} \t lon : {gps_data.gpgga.lon:.6f}\t alt : {gps_data.gpgga.alt:.4f}')
        
        time.sleep(0.1)

if __name__ == '__main__':
    main()
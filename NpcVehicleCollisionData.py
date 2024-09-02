import time
from lib.network.UDP import Receiver
from lib.define.NpcVehicleCollisionData import NpcVehicleCollisionData

IP = '127.0.0.1' 
PORT = 9108

import ctypes
print(ctypes.sizeof(NpcVehicleCollisionData()))
#Protocol정보
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/ros-1#id-(24.R2-ko)통신메시지프로토콜-NPCVehicleCollisionData.1
def main():
    npc_vehicle_collision = Receiver(IP, PORT, NpcVehicleCollisionData())

    while True :
        npc_vehicle_collision_data = npc_vehicle_collision.get_data()
        print(npc_vehicle_collision_data)
        time.sleep(0.1)

if __name__ == '__main__':
    main()
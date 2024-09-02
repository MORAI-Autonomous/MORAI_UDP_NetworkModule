import time
from lib.network.UDP import Receiver
from lib.define.ObjectInfo import ObjectInfo

IP = '127.0.0.1' 
PORT = 7505

#Protocol 정보
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/ros-1#id-(24.R2-ko)통신메시지프로토콜-ObjectInfo.1
def main():
    obj_info = Receiver(IP, PORT, ObjectInfo())
    while True :
        obj_data = obj_info.get_data()        
        print(obj_data) 
        _print(obj_data) 

        time.sleep(0.1)

def _print(obj_data):
    if not obj_data == None:
        for obj in obj_data.data:
            if obj.obj_id == 0 :
                break
            else:
                print(obj)
                print("\n")

if __name__ == '__main__':
    main()
import cv2
import numpy as np
from lib.network.UDP import Receiver
from lib.define.Camera import Camera
import time

IP = '127.0.0.1' 
PORT = 1111

#Protocol 정보
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/-35#id-(24.R2-ko)센서통신프로토콜-UDP
def main():
    cam_data = Receiver(IP, PORT, Camera())
    is_boundingbox = True
    while True :
        
        data = cam_data.get_data()        
        try:
            image = cv2.imdecode(np.frombuffer(data.image.data, dtype=np.uint8), cv2.IMREAD_COLOR)
        except:
            continue
        cv2.imshow("MORAI Cam Parser", image)            

        #Bounding Box 데이터가 들어오고 있을 때 bbox 출력
        
        if is_boundingbox and time.time() - data.bbox_timestamp < 1: 
            #Resolution 세팅
            data.utils.setResolution(w = 640, h = 480, fov = 90)

            bbox_info = data.bbox
            _2d_bb_img = image.copy()
            _3d_bb_img = image.copy()
            
            for bbox_info in bbox_info.object_data:                                    
                if bbox_info.Group == 0 and bbox_info.Class == 0 and bbox_info.SubClass == 0 :                    
                    break
                
                color = (bbox_info.Group, bbox_info.Class, bbox_info.SubClass)
                
                #2d bbox                          
                point_2 = (int(bbox_info._2D_BBOX_XMAX), int(bbox_info._2D_BBOX_YMAX))
                point_1 = (int(bbox_info._2D_BBOX_XMIN), int(bbox_info._2D_BBOX_YMIN))                
                data.utils.draw_2d_bbox(_2d_bb_img, point_1, point_2, color)

                #3d bbox
                point_list = data.utils.projectPoints(bbox_info)
                data.utils.draw_3d_bbox(_3d_bb_img, point_list, color)
            
            cv2.imshow("2D BBox", _2d_bb_img)         
            cv2.imshow("3D BBox", _3d_bb_img)
        else:
            try:
                cv2.destroyWindow("2D BBox")         
                cv2.destroyWindow("3D BBox")
            except:
                pass
        
        cv2.waitKey(1)


if __name__ == '__main__':
    main()
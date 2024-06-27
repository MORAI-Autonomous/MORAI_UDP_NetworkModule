

import time
from lib.UDP import udp_sender
from lib.EGO_Ghost_Mode_util import util

class EGO_GHOST_MANAGER :

    def __init__(self):        
        self.udp_socket = udp_sender('127.0.0.1', 9097, 'ego_ghost')

        self.ghost_manager = util()
        x = 0 
        y = 0 
        z = 0
        while True:
            
            data = [x + 0, y + 0, z + 0, 0, 0, 0, 0, 0]

            x += 1
            y += 1
            z += 1
            
            udp_packet = self.ghost_manager.unpack_data(data)
            self.udp_socket.send_data(udp_packet)
            time.sleep(1)
        
if __name__ == "__main__":
    EGO_GHOST_MANAGER()

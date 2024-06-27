

import time
from lib.UDP import udp_sender
from lib.NPC_Ghost_Mode_util import util

class NPC_GHOST_MANAGER :

    def __init__(self):        
        self.udp_socket = udp_sender('127.0.0.1', 7604, 'npc_ghost')
        self.ghost_manager = util()
        x = 13
        y = 1100 
        z = 0

        while True:            
            data = [
                [1, '2015_Kia_K5              ', x + 0, y + 0, z + 0, 0, 0, 0],
                [2, '2015_Kia_K5              ', x + 5, y + 5, z + 5, 0, 0, 0],
                [3, '2015_Kia_K5              ', x + 10, y + 10, z + 10, 0, 0, 0],
                [4, '2015_Kia_K5              ', x + 15, y + 15, z + 15, 0, 0, 0],
                [5, '2015_Kia_K5              ', x + 20, y + 20, z + 20, 0, 0, 0],
                [6, '2015_Kia_K5              ', x + 25, y + 25, z + 25, 0, 0, 0],
                [7, '2015_Kia_K5              ', x + 30, y + 30, z + 30, 0, 0, 0],
                [8, '2015_Kia_K5              ', x + 35, y + 35, z + 35, 0, 0, 0],
                [9, '2015_Kia_K5              ', x + 40, y + 40, z + 40, 0, 0, 0],
                [10, '2015_Kia_K5              ', x + 45, y + 45, z + 45, 0, 0, 0],
                [11, '2015_Kia_K5              ', x + 50, y + 50, z + 50, 0, 0, 0],
                [12, '2015_Kia_K5              ', x + 55, y + 55, z + 55, 0, 0, 0],
                [13, '2015_Kia_K5              ', x + 60, y + 60, z + 60, 0, 0, 0],
                [14, '2015_Kia_K5              ', x + 65, y + 65, z + 65, 0, 0, 0],
                [15, '2015_Kia_K5              ', x + 70, y + 70, z + 70, 0, 0, 0],
                [16, '2015_Kia_K5              ', x + 75, y + 75, z + 75, 0, 0, 0],
                [17, '2015_Kia_K5              ', x + 80, y + 80, z + 80, 0, 0, 0],
                [18, '2015_Kia_K5              ', x + 85, y + 85, z + 85, 0, 0, 0],
                [19, '2015_Kia_K5              ', x + 90, y + 90, z + 90, 0, 0, 0],
                [20, '2015_Kia_K5              ', x + 95, y + 95, z + 95, 0, 0, 0],
            ]

            x += 1
            y += 1
            z += 1

            udp_packet = self.ghost_manager.unpack_data(data)
            self.udp_socket.send_data(udp_packet)

            time.sleep(1)
        
if __name__ == "__main__":
    NPC_GHOST_MANAGER()
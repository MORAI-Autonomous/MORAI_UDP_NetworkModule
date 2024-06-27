import struct

class util :
    def __init__(self):

        header = '#NpcGhostCmd$'.encode()
        data_length = struct.pack('i', 1000)
        aux_data = struct.pack('3i', 0, 0, 0)
        self.upper = header + data_length + aux_data
        self.tail = '\r\n'.encode()
        

    def unpack_data(self,data):
        lower = b''

        for i in range(20):
            packed_id = struct.pack('b', data[i][0])
            packed_name = data[i][1].encode()
            packed_x = struct.pack('f', data[i][2])
            packed_y = struct.pack('f', data[i][3])
            packed_z = struct.pack('f', data[i][4])
            packed_roll = struct.pack('f', data[i][5])
            packed_picth = struct.pack('f', data[i][6])
            packed_yaw = struct.pack('f', data[i][7])

            lower += packed_id + packed_name + packed_x + packed_y + packed_z + packed_roll + packed_picth + packed_yaw

        send_data = self.upper + lower + self.tail
        return send_data
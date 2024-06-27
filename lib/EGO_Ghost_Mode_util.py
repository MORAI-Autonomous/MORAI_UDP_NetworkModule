import struct

class util:

    def __init__(self):
        header = '#EgoGhostCmd$'.encode()
        data_length = struct.pack('i', 32)
        aux_data = struct.pack('3i', 0, 0, 0)
        self.upper = header + data_length + aux_data
        self.tail = '\r\n'.encode()

    def unpack_data(self,data):
        packed_x = struct.pack('f', data[0])
        packed_y = struct.pack('f', data[1])
        packed_z = struct.pack('f', data[2])
        packed_roll = struct.pack('f', data[3])
        packed_picth = struct.pack('f', data[4])
        packed_yaw = struct.pack('f', data[5])
        packed_vel = struct.pack('f', data[6])
        packed_steer = struct.pack('f', data[7])

        lower = packed_x + packed_y + packed_z + packed_roll + packed_picth + packed_yaw + packed_vel + packed_steer

        send_data = self.upper + lower + self.tail
        return send_data
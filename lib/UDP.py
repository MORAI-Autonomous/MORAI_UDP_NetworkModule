import socket

class udp_sender :
    def __init__(self,ip,port,data_type):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ip=ip
        self.port=port
        self.data_type=data_type

    def send_data(self,send_data):
        self.sock.sendto(send_data,(self.ip,self.port))    
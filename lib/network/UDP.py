import socket
import ctypes
import multiprocessing
import threading

class Receiver :
    def __init__(self, ip, port, data_type):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 2**20) # 1MB 
        self.socket.bind((ip,port))

        self.data_type = data_type
        self.parsed_data = data_type

        self.data_size = ctypes.sizeof(data_type)

        self.parsed_data_queue = multiprocessing.Queue()
        threading.Thread(target=self.data_parsing, daemon=True).start()
        multiprocessing.Process(target=self.recv_udp_data, daemon=True).start()

        

    def recv_udp_data(self):        
        while True :
            raw_data, _ = self.socket.recvfrom(self.data_size)            
            ctypes.memmove(ctypes.addressof(self.data_type), raw_data, self.data_size)            
            try:#한번에 여러 데이터가 들어오는 protocol을 위해 별도의 parsing(CAM, GPS 등등..)
                self.data_type.parsing()
            except Exception as e :
                pass            
            self.parsed_data_queue.put(self.data_type)

    def data_parsing(self) :
        while True:
            self.parsed_data = self.parsed_data_queue.get()
        
        
    def get_data(self) :
        return self.parsed_data

    def __del__(self):
        self.socket.close()        
        print('del')

class Sender:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, data):
        pacekd_data = ctypes.string_at(ctypes.addressof(data), ctypes.sizeof(data))       
        print(pacekd_data, len(pacekd_data))
        self.socket.sendto(pacekd_data,(self.ip,self.port))
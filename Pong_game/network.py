import socket
import pickle

class Network :
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        self.server = "Your IPv4 address"
        self.port = 5555
        self.addr = (self.server , self.port)
        self.p , self.b = self.connect()
    

    def getP(self):
        return self.p
    
    def getB(self):
        return self.b
    
    def connect(self) :
        try :
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(8192))
        except :
            pass
            
    def send(self , data):
        try :
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(8192))
        except socket.error as e :
            print(e)

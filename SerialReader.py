import threading
import serial

connected = False
port = '/home/calata/reader'
baud = 9600
buffer = b''


class SerialReader:
    def __init__(self, port, baud=9600, callback=None):
        self.__port = port
        self.__baud = baud
        self.__buffer = b''
        self.__calback = callback
        self.__connected = True
        self.__serial = serial.Serial(port, baud, timeout=0)

    def launch_read(self):
        self.thread = threading.Thread(target=self.__read_from_port)
        self.thread.start()

    def __read_from_port(self):
        while True:
            self.__buffer += self.__serial.read(1)
            if len(self.__buffer) is not 0:
                if b'\r\n' in self.__buffer and b'!' in self.__buffer:
                    possible_packet = self.__buffer.split(b'!')[1]
                    if self.__calback is not None:
                        self.__calback(possible_packet)
                    self.__buffer = b''
                elif b'\r\n' in self.__buffer and not (b'!' in buffer):
                    self.__buffer = b''



def handle_data(data):
    print(data.decode('ascii'))


if __name__ == "__main__":
    serialReader = SerialReader(port,baud,handle_data)
    serialReader.launch_read()

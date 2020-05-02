import socket
import pickle


class ServerCommunication:
    def __init__(self):
        self.__socket = None
        self.__header_size = 16
        self.__code_size = 2

    def initialize_soket(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect((socket.gethostname(), 8080))

    def get_socket(self):
        return self.__socket

    def read_from_server(self, data_type):
        message_lenght = None
        data_received = b""
        new_data = True
        while True:
            data = self.__socket.recv(8)
            if new_data:
                not_empty = False
                for e in data[:self.__header_size]:
                    if e != ' ':
                        not_empty = True
                if not_empty:
                    message_lenght = int(data[:self.__header_size])
                new_data = False
            data_received += data

            if message_lenght is not None and message_lenght != 0:
                if len(data_received) - self.__header_size == message_lenght:
                    print("Received data of type: ", end="")
                    if data_type == 0:
                        print("employee.")
                        employees = pickle.loads(data_received[self.__header_size:])
                        return employees
                    elif data_type == 1:
                        print("location.")
                        locations = pickle.loads(data_received[self.__header_size:])
                        return locations

    def write_to_server(self, code, data):
        self.write_action_code(code)
        self.write_data(data)

    def write_action_code(self, code):
        code = str(code)
        data = bytes(code, "utf-8")
        self.__socket.send(data)
        print("Code sent.")

    def write_data(self, data):
        serialized_data = pickle.dumps(data)
        message = bytes(f"{len(serialized_data):<{self.__header_size}}", "utf-8") + serialized_data
        self.__socket.send(message)
        print("Data sent.")

    def communicate(self, code, data):
        self.write_to_server(code, data)
        employees = self.read_from_server(0)
        locations = self.read_from_server(1)
        return employees, locations

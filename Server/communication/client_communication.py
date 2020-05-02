import socket
import time
import pickle


class ClientCommunication:
    def __init__(self, location_persistence, employee_persistence):
        self.__location_persistance = location_persistence
        self.__employee_persistance = employee_persistence
        self.__socket = None
        self.__header_size = 16
        self.__client_socket = None
        self.__address = None

    def initialize_soket(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((socket.gethostname(), 8080))
        self.__socket.listen(1)
        self.__client_socket, self.__address = self.__socket.accept()

    def get_socket(self):
        return self.__socket

    def read_code(self):
        code_received = self.__client_socket.recv(2)
        if len(code_received) != 0:
            code_received = int(code_received)
            print("Received code: " + str(code_received) + ".")
            return code_received

    def read_data(self):
        data_received = b""
        new_data = True
        message_lenght = 0
        while True:
            data = self.__client_socket.recv(8)
            if new_data:
                not_empty = False
                for e in data[:self.__header_size]:
                    if e != ' ':
                        not_empty = True
                if not_empty:
                    message_lenght = int(data[:self.__header_size])
                new_data = False
            data_received += data

            if message_lenght != 0:
                if len(data_received) - self.__header_size == message_lenght:
                    print("Received data from client.")
                    deserialized = pickle.loads(data_received[self.__header_size:])
                    return deserialized

    def write_to_client(self):
        serialized_employees = pickle.dumps(self.__employee_persistance.get_data())
        message = bytes(f"{len(serialized_employees):<{self.__header_size}}", "utf-8") + serialized_employees
        self.__client_socket.send(message)
        print("Employees sent.")
        time.sleep(0.1)
        serialized_locations = pickle.dumps(self.__location_persistance.get_data())
        message = bytes(f"{len(serialized_locations):<{self.__header_size}}", "utf-8") + serialized_locations
        self.__client_socket.send(message)
        print("Locations sent.")

    def read_from_client(self):
        code = self.read_code()
        data = self.read_data()
        return code, data

    def communicate(self):
        while True:
            code, data = self.read_from_client()
            if code == 0:
                self.__employee_persistance.set_new_password(data[0], data[1], data[2], data[3])
            elif code == 1:
                self.__location_persistance.update_location(data[0], data[1], data[2])
            elif code == 2:
                self.__location_persistance.add_location(data[0], data[1], data[2])
            elif code == 3:
                self.__location_persistance.delete_location(data[0])
            elif code == 4:
                self.__employee_persistance.set_location(data[0], data[1], data[2])
            elif code == 5:
                self.__employee_persistance.add_employee(data[0], data[1], data[2])
            elif code == 6:
                self.__employee_persistance.set_coordinator(data[0], data[1], data[2], data[3])
            elif code == 7:
                self.__employee_persistance.delete_employee(data[0], data[1], data[2])
            elif code == 8:
                self.__employee_persistance.update_employee(data[0], data[1], data[2], data[3], data[4])
            self.write_to_client()

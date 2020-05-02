from databse_access.manager import Manager
from databse_access.employee_persistence import EmployeePersistence
from databse_access.location_persistence import LocationPersistence
from communication.client_communication import ClientCommunication


class ControllerServer:
    def __init__(self, reinitialize_database):
        self.__location_persistance = LocationPersistence()
        self.__employee_persistance = EmployeePersistence()
        if reinitialize_database:
            Manager.recreate_database(self.__location_persistance, self.__employee_persistance)
        self.__client_communication = ClientCommunication(self.__location_persistance, self.__employee_persistance)
        self.__client_communication.initialize_soket()
        self.__client_communication.write_to_client()
        self.__client_communication.communicate()


server_controller = ControllerServer(False)

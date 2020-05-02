from data_processing.employees_processing import EmployeesProcessing
from data_processing.locations_processing import LocationsProcessing


class ProcessingBuilder:
    def __init__(self, server_communication):
        self.__employees_processing = EmployeesProcessing(server_communication)
        self.__locations_processing = LocationsProcessing(server_communication)

    def get_employees_processing(self):
        return self.__employees_processing

    def get_locations_processing(self):
        return self.__locations_processing

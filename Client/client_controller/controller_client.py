from communication.server_communication import ServerCommunication
from views.base_view import BaseView
from views.login_view import LoginView
from data_processing.processing_builder import ProcessingBuilder
from client_controller.login_controller import LoginController


class ControllerClient:
    def __init__(self):
        self.__server_communication = ServerCommunication()
        self.__processing_builder = ProcessingBuilder(self.__server_communication)
        self.__server_communication.initialize_soket()
        employees = self.__server_communication.read_from_server(0)
        self.__processing_builder.get_employees_processing().set_employees(employees)
        locations = self.__server_communication.read_from_server(1)
        self.__processing_builder.get_locations_processing().set_locations(locations)

        self.__base_view = BaseView()
        self.__login_view = LoginView(self.__base_view.get_window())
        self.__lc = LoginController(self.__login_view, self.__base_view, self.__processing_builder)
        self.__lc.login_button_listener()
        self.__lc.display_login_interface()


if __name__ == "__main__":
    clientController = ControllerClient()

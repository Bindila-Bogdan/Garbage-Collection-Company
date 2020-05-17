from views.employee_view import EmployeeView
from client_controller.employee_controller import EmployeeController
from views.coordinator_view import CoordinatorView
from client_controller.coordinator_controller import CoordinatorController
from views.administrator_view import AdmnistratorView
from client_controller.administrator_controller import AdministratorController
from map_processing.route_generator import RouteGenerator

debug = False


# username = "administrator_Bindila_Bogdan"
# password = "administrator_default"

# username = "coordinator_Conan_Myles"
# password = "coordinator_default"

# username = "employee_Dominic_Vega"
# password = "employee_default"


class LoginController:
    def __init__(self, login_view, base_view, processing_builder, language_subject):
        self.__login_view = login_view
        self.__login_window = self.__login_view.get_login_window()
        self.__processing_builder = processing_builder
        self.__base_view = base_view
        self.__language_subject = language_subject
        self.__language_subject.attach(login_view)
        self.__language_subject.set_language("romanian")
        self.__language_subject.notify()
        self.language_buttons_listeners()

    def language_buttons_listeners(self):
        french_language_button = self.__login_view.get_french_language_button()
        french_language_button.config(command=self.french_language_required)

        english_language_button = self.__login_view.get_english_language_button()
        english_language_button.config(command=self.english_language_required)

        romanian_language_button = self.__login_view.get_romanian_language_button()
        romanian_language_button.config(command=self.romanian_language_required)

        spanish_language_button = self.__login_view.get_spanish_language_button()
        spanish_language_button.config(command=self.spanish_language_required)

    def login_button_listener(self):
        login_button = self.__login_view.get_login_button()
        login_button.configure(command=self.get_credentials)

    def get_credentials(self):
        username_field = self.__login_view.get_username_text_field()
        password_field = self.__login_view.get_password_text_field()
        username = username_field.get()
        password = password_field.get()
        if debug:
            username = "employee_Dominic_Vega"
            password = "employee_default"

        account, employee = self.__processing_builder.get_employees_processing().search_for_account(username, password)
        if account is not None:
            self.__login_view.clean()
            self.__language_subject.detach(self.__login_view)
            route_gen = RouteGenerator(self.__processing_builder.get_locations_processing().get_locations())
            if account.get_account_type() == "employee":
                self.generate_employee_interface(route_gen, employee)
            elif account.get_account_type() == "coordinator":
                self.generate_coordinator_interface(route_gen, employee)
            elif account.get_account_type() == "administrator":
                self.generate_administrator_interface(employee)
        else:
            self.__login_view.show_warning()

    def generate_employee_interface(self, route_gen, employee):
        print("Employee")
        frame = EmployeeView(self.__base_view.get_window(), route_gen)
        self.__language_subject.attach(frame)
        self.__language_subject.notify()
        ec = EmployeeController(frame, self.__processing_builder, employee, self.__language_subject)
        ec.set_coordinator_name_label()
        ec.set_name_label()
        ec.set_location_label()
        ec.generate_route_listener()
        ec.change_password_listener()
        ec.language_buttons_listeners()

    def generate_coordinator_interface(self, route_gen, employee):
        print("Coordinator")
        frame = CoordinatorView(self.__base_view.get_window(), route_gen)
        self.__language_subject.attach(frame)
        self.__language_subject.notify()
        cc = CoordinatorController(frame, self.__processing_builder, employee, route_gen, self.__language_subject)
        cc.set_name_label()
        cc.generate_route_listener()
        cc.change_password_listener()
        cc.csv_report_button_listener()
        cc.json_report_button_listener()
        cc.xml_report_button_listener()
        cc.update_employees_table()
        cc.update_assigned_location_button_listener()
        cc.update_locations_table()
        cc.update_locations_table()
        cc.update_locations_data_button_listener()
        cc.update_locations_table()
        cc.add_a_new_location_button_listener()
        cc.delete_a_location_button_listener()
        cc.tabs_listener()
        cc.language_buttons_listeners()

    def generate_administrator_interface(self, employee):
        print("Administrator")
        frame = AdmnistratorView(self.__base_view.get_window())
        self.__language_subject.attach(frame)
        self.__language_subject.notify()
        ac = AdministratorController(frame, self.__processing_builder, employee, self.__language_subject)
        ac.set_administrator_name_label()
        ac.change_password_button_listener()
        ac.delete_coordinator_button_listener()
        ac.add_new_coordinator_button_listener()
        ac.update_coordinator_button_listener()
        ac.add_new_employee_button_listener()
        ac.update_employee_button_listener()
        ac.delete_employee_button_listener()
        ac.update_employees_table()
        ac.update_coordinators_table()
        ac.tabs_listener()
        ac.language_buttons_listeners()

    def display_login_interface(self):
        self.__login_window.mainloop()

    def french_language_required(self):
        self.__language_subject.set_language("french")
        self.__language_subject.notify()

    def english_language_required(self):
        self.__language_subject.set_language("english")
        self.__language_subject.notify()

    def romanian_language_required(self):
        self.__language_subject.set_language("romanian")
        self.__language_subject.notify()

    def spanish_language_required(self):
        self.__language_subject.set_language("spanish")
        self.__language_subject.notify()

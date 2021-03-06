class EmployeeController:
    def __init__(self, employee_view, processing_builder, employee, language_subject):
        self.__employee_view = employee_view
        self.__employee = employee
        self.__employee_window = self.__employee_view.get_employee_window()
        self.__processing_builder = processing_builder
        self.__employees_data = self.__processing_builder.get_employees_processing()
        self.__locations_data = self.__processing_builder.get_locations_processing()
        self.__accounts_data = self.__employees_data.get_accounts()
        self.__language_subject = language_subject

    def language_buttons_listeners(self):
        french_language_button = self.__employee_view.get_french_language_button()
        french_language_button.config(command=self.french_language_required)

        english_language_button = self.__employee_view.get_english_language_button()
        english_language_button.config(command=self.english_language_required)

        romanian_language_button = self.__employee_view.get_romanian_language_button()
        romanian_language_button.config(command=self.romanian_language_required)

        spanish_language_button = self.__employee_view.get_spanish_language_button()
        spanish_language_button.config(command=self.spanish_language_required)

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

    def change_password_listener(self):
        change_password_button = self.__employee_view.get_change_password_button()
        change_password_button.config(command=self.process_password)

    def generate_route_listener(self):
        route_button = self.__employee_view.get_generate_route_button()
        route_button.config(command=self.generate_route)

    def display_employee_interface(self):
        self.__employee_window.mainloop()

    def process_password(self):
        old_password_field = self.__employee_view.get_password_field()
        new_password_field = self.__employee_view.get_new_password_field()
        old_password = old_password_field.get()
        new_password = new_password_field.get()
        for employee in self.__employees_data.get_employees():
            if employee == self.__employee:
                if employee.get_account().get_password() == old_password:
                    employee.get_account().set_password(new_password)
                    self.__employees_data.update_password(employee.get_first_name(),
                                                          employee.get_last_name(), new_password, True)

    def generate_route(self):
        locations = self.__locations_data.get_locations()
        number_of_locations = len(locations)
        self.__employee_view.plot_route(number_of_locations)

    def set_name_label(self):
        full_name = self.__employee_view.get_acctual_name_label()
        full_name.configure(text=self.__employee.get_first_name() + " " + self.__employee.get_last_name())

    def set_coordinator_name_label(self):
        coordinator_label = self.__employee_view.get_acctual_coordinator_label()
        coordinator = self.__employee.get_coordinator()
        coordinator_label.configure(text=coordinator)

    def set_location_label(self):
        location_label = self.__employee_view.get_acctual_location_label()
        location_label.configure(text=self.__employee.get_location())

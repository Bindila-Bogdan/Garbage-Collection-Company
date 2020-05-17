from model.employee import Employee
from reports.report_builder import ReportBuilder


class CoordinatorController:
    def __init__(self, coordinator_view, processing_builder, coordinator, route_gen, language_subject):
        self.__coordinator_view = coordinator_view
        self.__coordinator = coordinator
        self.__coordinator_window = self.__coordinator_view.get_coordinator_window()
        self.__processing_builder = processing_builder
        self.__reports = ReportBuilder()
        self.__csv_reports = self.__reports.get_csv_report()
        self.__json_reports = self.__reports.get_json_report()
        self.__xml_reports = self.__reports.get_xml_report()
        self.__route_gen = route_gen
        self.__employees_data = self.__processing_builder.get_employees_processing()
        self.__locations_data = self.__processing_builder.get_locations_processing()
        self.__language_subject = language_subject

    def language_buttons_listeners(self):
        french_language_button = self.__coordinator_view.get_french_language_button()
        french_language_button.config(command=self.french_language_required)

        english_language_button = self.__coordinator_view.get_english_language_button()
        english_language_button.config(command=self.english_language_required)

        romanian_language_button = self.__coordinator_view.get_romanian_language_button()
        romanian_language_button.config(command=self.romanian_language_required)

        spanish_language_button = self.__coordinator_view.get_spanish_language_button()
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
        change_password_button = self.__coordinator_view.get_change_password_button()
        change_password_button.configure(command=self.process_password)

    def generate_route_listener(self):
        route_button = self.__coordinator_view.get_generate_route_button()
        route_button.configure(command=self.generate_route)

    def csv_report_button_listener(self):
        csv_button = self.__coordinator_view.get_csv_report_button()
        csv_button.configure(command=self.generate_csv_report)

    def json_report_button_listener(self):
        json_button = self.__coordinator_view.get_json_report_button()
        json_button.configure(command=self.generate_json_report)

    def xml_report_button_listener(self):
        xml_button = self.__coordinator_view.get_xml_report_button()
        xml_button.configure(command=self.generate_xml_report)

    def update_assigned_location_button_listener(self):
        update_button = self.__coordinator_view.get_update_employees_locations_button()
        update_button.configure(command=self.update_employees_data)

    def update_locations_data_button_listener(self):
        update_button = self.__coordinator_view.get_update_locations_button()
        update_button.configure(command=self.update_locations_data)

    def add_a_new_location_button_listener(self):
        add_a_new_location_button = self.__coordinator_view.get_add_new_location_button()
        add_a_new_location_button.configure(command=self.add_a_new_location)

    def delete_a_location_button_listener(self):
        delete_a_location_name_field = self.__coordinator_view.get_delete_location_button()
        delete_a_location_name_field.configure(command=self.delete_a_location)

    def tabs_listener(self):
        tabs = self.__coordinator_view.get_tabs()
        tabs.bind("<<NotebookTabChanged>>", self.cleaning_tables)

    def set_name_label(self):
        full_name = self.__coordinator_view.get_acctual_name_label()
        full_name.configure(text=self.__coordinator.get_first_name() + " " + self.__coordinator.get_last_name())

    def set_coordinator_name_label(self):
        coordinator_label = self.__coordinator_view.get_acctual_coordinator_label()
        coordinator = self.__coordinator.get_coordinator()
        coordinator_label.configure(text=coordinator)

    def process_password(self):
        old_password_field = self.__coordinator_view.get_password_field()
        new_password_field = self.__coordinator_view.get_new_password_field()
        old_password = old_password_field.get()
        new_password = new_password_field.get()
        for employee in self.__employees_data.get_employees():
            if employee == self.__coordinator:
                if employee.get_account().get_password() == old_password:
                    employee.get_account().set_password(new_password)
                    self.__employees_data.update_password(employee.get_first_name(),
                                                          employee.get_last_name(), new_password, False)

    def generate_route(self):
        locations = self.__locations_data.get_locations()
        number_of_locations = len(locations)
        self.__coordinator_view.plot_route(number_of_locations)

    def __prepare_data(self):
        locations = self.__locations_data.get_locations()
        employees = self.__employees_data.get_employees()
        self.__reports.generate_locations_data(locations, employees)

    def generate_csv_report(self):
        self.__prepare_data()
        self.__csv_reports.write_in_csv_file(
            self.__coordinator.get_first_name() + "_" + self.__coordinator.get_last_name())

    def generate_json_report(self):
        self.__prepare_data()
        self.__json_reports.write_in_json_file(
            self.__coordinator.get_first_name() + "_" + self.__coordinator.get_last_name())

    def generate_xml_report(self):
        self.__prepare_data()
        self.__xml_reports.write_in_xml_file(
            self.__coordinator.get_first_name() + "_" + self.__coordinator.get_last_name())

    def update_employees_table(self):
        coordinator_name = self.__coordinator.get_first_name() + " " + self.__coordinator.get_last_name()
        employees = self.__employees_data.get_coordintated_employees(coordinator_name)
        number_of_employees = len(employees)
        employees_table = self.__coordinator_view.get_employees_table()
        for row in range(1, len(employees_table) - 1):
            for column in range(1, len(employees_table[row])):
                if column == 3:
                    employees_table[row][column].config(text="")
        for row in range(1, len(employees_table) - 1):
            for column in range(1, len(employees_table[row])):
                if row <= number_of_employees:
                    if column == 1:
                        employees_table[row][column].configure(text=employees[row - 1].get_first_name())
                    elif column == 2:
                        employees_table[row][column].configure(text=employees[row - 1].get_last_name())
                    elif column == 3:
                        pass
                        employees_table[row][column].delete(0, 'end')
                        employees_table[row][column].insert(0, employees[row - 1].get_location())
                if row >= number_of_employees + 1:
                    if column == 1:
                        employees_table[row][column].configure(text="")
                    elif column == 2:
                        employees_table[row][column].configure(text="")
                    elif column == 3:
                        employees_table[row][column].delete(0, 'end')

    def check_location(self, assigned_location):
        locations = self.__locations_data.get_locations()
        for location in locations:
            if str(location.get_name()) == str(assigned_location):
                return True
        return False

    def unique_location(self, location):
        employees = self.__employees_data.get_employees()
        for employee in employees:
            if isinstance(employee, Employee):
                if str(employee.get_location()) == str(location):
                    return False
        return True

    def update_employees_data(self):
        coordinator_name = self.__coordinator.get_first_name() + " " + self.__coordinator.get_last_name()
        employees = self.__employees_data.get_coordintated_employees(coordinator_name)
        number_of_employees = len(employees)
        employees_table = self.__coordinator_view.get_employees_table()
        for row in range(1, len(employees_table)):
            for column in range(3, 0, -1):
                if row <= number_of_employees:
                    if column == 3:
                        assigned_location = employees_table[row][column].get()
                        if assigned_location == "-":
                            self.__employees_data.assign_location(employees[row - 1].get_first_name(),
                                                                  employees[row - 1].get_last_name(),
                                                                  None)
                        elif self.check_location(assigned_location) and self.unique_location(assigned_location):
                            self.__employees_data.assign_location(employees[row - 1].get_first_name(),
                                                                  employees[row - 1].get_last_name(),
                                                                  assigned_location)
        self.update_employees_table()

    def assignation(self, location):
        for employee in self.__employees_data.get_employees():
            if isinstance(employee, Employee):
                if str(employee.get_location()) == str(location.get_name()):
                    return employee.get_first_name() + " " + employee.get_last_name()
        return "-"

    def check_assignation(self, full_employee_name, coordinator):
        for employee in self.__employees_data.get_employees():
            if isinstance(employee, Employee):
                if str(employee.get_first_name() + " " + employee.get_last_name()) == str(full_employee_name):
                    if employee.get_coordinator() == coordinator.get_first_name() + " " + coordinator.get_last_name():
                        return True
        return False

    def update_locations_data(self):
        locations = self.__locations_data.get_locations()
        number_of_locations = len(locations)
        locations_table = self.__coordinator_view.get_locations_table()
        for row in range(1, len(locations_table)):
            for column in range(1, 5):
                if row <= number_of_locations:
                    if column == 1:
                        location_name = locations_table[row][column]["text"]
                    elif column == 2:
                        full_employee_name = locations_table[row][column]["text"]
                    elif column == 3:
                        ox_coord = locations_table[row][column].get()
                    elif column == 4:
                        oy_coord = locations_table[row][column].get()
            if full_employee_name == "-" or self.check_assignation(full_employee_name, self.__coordinator):
                if len(location_name) != 0 and CoordinatorController.is_number(ox_coord) and \
                        CoordinatorController.is_number(oy_coord):
                    self.__locations_data.modify_current_location(location_name, ox_coord, oy_coord)
        self.update_locations_table()

    def update_locations_table(self):
        locations = self.__locations_data.get_locations()
        self.__route_gen.set_locations_and_regenerate_map(locations)
        number_of_locations = len(locations)
        locations_table = self.__coordinator_view.get_locations_table()
        for row in range(1, len(locations_table) - 1):
            for column in range(1, len(locations_table[row])):
                if row <= number_of_locations:
                    if column == 1:
                        locations_table[row][column].configure(text=str(locations[row - 1].get_name()))
                    elif column == 2:
                        locations_table[row][column].configure(text=self.assignation(locations[row - 1]))
                    elif column == 3:
                        locations_table[row][column].delete(0, 'end')
                        locations_table[row][column].insert(0, str(locations[row - 1].get_coord_ox()))
                    elif column == 4:
                        locations_table[row][column].delete(0, 'end')
                        locations_table[row][column].insert(0, str(locations[row - 1].get_coord_oy()))
                if row >= number_of_locations + 1:
                    if column == 1:
                        locations_table[row][column].configure(text="")
                    elif column == 2:
                        locations_table[row][column].configure(text="")
                    elif column == 3:
                        locations_table[row][column].delete(0, 'end')
                    elif column == 4:
                        locations_table[row][column].delete(0, 'end')

    @staticmethod
    def is_number(number):
        try:
            float(number)
        except ValueError:
            return False
        return True

    def add_a_new_location(self):
        new_location_name_field = self.__coordinator_view.get_new_location_name()
        new_location_ox_coord_field = self.__coordinator_view.get_ox_coord()
        new_location_oy_coord_field = self.__coordinator_view.get_oy_coord()
        new_location_name = new_location_name_field.get()
        new_location_ox_coord = new_location_ox_coord_field.get()
        new_location_oy_coord = new_location_oy_coord_field.get()
        if len(new_location_name) != 0 and CoordinatorController.is_number(new_location_ox_coord) and \
                CoordinatorController.is_number(new_location_oy_coord):
            self.__locations_data.add_current_location(new_location_name, new_location_ox_coord,
                                                       new_location_oy_coord)
        self.update_locations_table()

    def delete_a_location(self):
        location_name_field = self.__coordinator_view.get_location_name()
        location_name = location_name_field.get()
        if len(location_name) != 0 and CoordinatorController.is_number(location_name):
            self.__locations_data.delete_current_location(location_name)
        self.update_locations_table()
        self.update_employees_table()

    def cleaning_tables(self, event):
        self.update_employees_table()
        self.update_locations_table()
        self.__coordinator_view.change_image()

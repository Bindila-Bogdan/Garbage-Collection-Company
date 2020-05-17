class AdministratorController:
    def __init__(self, administrator_view, processing_builder, administrator, language_subject):
        self.__administrator_view = administrator_view
        self.__administrator = administrator
        self.__administrator_window = self.__administrator_view.get_administrator_window()
        self.__processing_builder = processing_builder
        self.__employees_data = self.__processing_builder.get_employees_processing()
        self.__locations_data = self.__processing_builder.get_locations_processing()
        self.__language_subject = language_subject

    def language_buttons_listeners(self):
        french_language_button = self.__administrator_view.get_french_language_button()
        french_language_button.config(command=self.french_language_required)

        english_language_button = self.__administrator_view.get_english_language_button()
        english_language_button.config(command=self.english_language_required)

        romanian_language_button = self.__administrator_view.get_romanian_language_button()
        romanian_language_button.config(command=self.romanian_language_required)

        spanish_language_button = self.__administrator_view.get_spanish_language_button()
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

    def change_password_button_listener(self):
        change_password_button = self.__administrator_view.get_change_admin_password_button()
        change_password_button.configure(command=self.process_password)

    def add_new_coordinator_button_listener(self):
        new_coordinator_button = self.__administrator_view.get_add_coordinator_button()
        new_coordinator_button.config(command=self.add_new_coordinator)

    def update_coordinator_button_listener(self):
        update_coordinator_button = self.__administrator_view.get_update_coordinator_button()
        update_coordinator_button.configure(command=self.update_coordinators)

    def delete_coordinator_button_listener(self):
        delete_coordinator_button = self.__administrator_view.get_delete_coordinator_button()
        delete_coordinator_button.configure(command=self.delete_coordinator)

    def add_new_employee_button_listener(self):
        new_employee_button = self.__administrator_view.get_add_employee_button()
        new_employee_button.config(command=self.add_new_employee)

    def update_employee_button_listener(self):
        update_employee_button = self.__administrator_view.get_update_employee_button()
        update_employee_button.configure(command=self.update_employees)

    def delete_employee_button_listener(self):
        delete_employee_button = self.__administrator_view.get_delete_employee_button()
        delete_employee_button.configure(command=self.delete_employee)

    def tabs_listener(self):
        tabs = self.__administrator_view.get_tabs()
        tabs.bind("<<NotebookTabChanged>>", self.cleaning_tables)

    def set_administrator_name_label(self):
        administrator_label = self.__administrator_view.get_acctual_administrator_label()
        administrator = self.__administrator.get_first_name() + " " + self.__administrator.get_last_name()
        administrator_label.configure(text=administrator)

    def process_password(self):
        old_password_field = self.__administrator_view.get_password_field()
        new_password_field = self.__administrator_view.get_new_password_field()
        old_password = old_password_field.get()
        new_password = new_password_field.get()
        for employee in self.__employees_data.get_employees():
            if employee == self.__administrator:
                if employee.get_account().get_password() == old_password:
                    employee.get_account().set_password(new_password)
                    self.__employees_data.update_password(employee.get_first_name(),
                                                          employee.get_last_name(), new_password, None)

    def cleaning_tables(self, event):
        self.update_employees_table()
        self.update_coordinators_table()

    def add_new_employee(self):
        first_name_field = self.__administrator_view.get_employee_first_name_field()
        last_name_field = self.__administrator_view.get_employee_last_name_field()
        coordinator_field = self.__administrator_view.get_coordinator_for_employee()
        first_name = first_name_field.get()
        last_name = last_name_field.get()
        coordinator = coordinator_field.get()
        exists = self.__employees_data.search_employee(first_name, last_name)
        if not exists:
            if len(first_name) != 0 and len(last_name) != 0:
                self.__employees_data.add_employee(first_name, last_name, True)
        if len(coordinator) != 0:
            exists_coordinator = self.__employees_data.check_if_coordinator_exits(
                coordinator)
            if exists_coordinator:
                coordinator_name = coordinator.split()
                if len(first_name) != 0 and len(last_name) != 0 and \
                        len(coordinator_name[0]) != 0 and len(coordinator_name[1]) != 0:
                    self.__employees_data.assign_coordinator(first_name, last_name,
                                                             coordinator_name[0], coordinator_name[1])
        self.update_employees_table()

    def delete_employee(self):
        number_of_employee_field = self.__administrator_view.get_employee_number()
        number_of_employee = number_of_employee_field.get()
        employees_table = self.__administrator_view.get_employees_table()
        try:
            first_name = employees_table[int(number_of_employee)][1].get()
            last_name = employees_table[int(number_of_employee)][2].get()
            self.__employees_data.remove_employee(first_name, last_name, True)
        except ValueError:
            pass
        self.update_employees_table()

    def update_employees(self):
        employees = self.__employees_data.get_just_employees()
        number_of_employees = len(employees)
        employees_table = self.__administrator_view.get_employees_table()
        for row in range(1, len(employees_table)):
            for column in range(1, len(employees_table[row])):
                if row <= number_of_employees:
                    if column == 1:
                        updated_first_name = employees_table[row][column].get()
                    elif column == 2:
                        updated_last_name = employees_table[row][column].get()
                    elif column == 4:
                        updated_coordinator = employees_table[row][column].get()

            if row <= number_of_employees:
                self.__employees_data.modify_employee(employees[row - 1].get_first_name(),
                                                      employees[row - 1].get_last_name(),
                                                      updated_first_name, updated_last_name, True)
                if len(updated_coordinator) != 0:
                    if updated_coordinator == "-":
                        self.__employees_data.assign_coordinator(updated_first_name,
                                                                 updated_last_name,
                                                                 None, None)
                    else:
                        exists_coordinator = self.__employees_data.check_if_coordinator_exits(
                            updated_coordinator)
                        if exists_coordinator:
                            coordinator_name = updated_coordinator.split()
                            self.__employees_data.assign_coordinator(updated_first_name, updated_last_name,
                                                                     coordinator_name[0], coordinator_name[1])
        self.update_employees_table()

    def update_employees_table(self):
        employees = self.__employees_data.get_just_employees()
        number_of_employees = len(employees)
        employees_table = self.__administrator_view.get_employees_table()
        for row in range(1, len(employees_table) - 1):
            for column in range(1, len(employees_table[row])):
                if row <= number_of_employees:
                    if column == 1:
                        employees_table[row][column].delete(0, 'end')
                        employees_table[row][column].insert(0, employees[row - 1].get_first_name())
                    elif column == 2:
                        employees_table[row][column].delete(0, 'end')
                        employees_table[row][column].insert(0, employees[row - 1].get_last_name())
                    elif column == 3:
                        employees_table[row][column].configure(text=employees[row - 1].get_location())
                    elif column == 4:
                        employees_table[row][column].delete(0, 'end')
                        employees_table[row][column].insert(0, employees[row - 1].get_coordinator())
                if row >= number_of_employees + 1:
                    if column == 1:
                        employees_table[row][column].delete(0, 'end')
                    elif column == 2:
                        employees_table[row][column].delete(0, 'end')
                    elif column == 3:
                        employees_table[row][column].configure(text="")
                    elif column == 4:
                        employees_table[row][column].delete(0, 'end')

    @staticmethod
    def is_number(number):
        try:
            float(number)
        except ValueError:
            return False
        return True

    def delete_coordinator(self):
        number_of_coordinator_field = self.__administrator_view.get_number_of_coordinator_field()
        number_of_coordinator = number_of_coordinator_field.get()
        if len(number_of_coordinator) != 0 and AdministratorController.is_number(number_of_coordinator):
            coordinators_table = self.__administrator_view.get_coordinators_table()
            try:
                first_name = coordinators_table[int(number_of_coordinator)][1].get()
                last_name = coordinators_table[int(number_of_coordinator)][2].get()
                self.__employees_data.remove_employee(first_name, last_name, False)
            except ValueError:
                pass
        self.update_coordinators_table()

    def update_coordinators(self):
        # update DB
        coordinators = self.__employees_data.get_coordinators()
        number_of_coordinators = len(coordinators)
        coordinators_table = self.__administrator_view.get_coordinators_table()
        for row in range(1, len(coordinators_table)):
            for column in range(1, len(coordinators_table[row])):
                if row <= number_of_coordinators:
                    if column == 1:
                        updated_first_name = coordinators_table[row][column].get()
                    elif column == 2:
                        updated_last_name = coordinators_table[row][column].get()
            if row <= number_of_coordinators:
                if len(coordinators[row - 1].get_first_name()) != 0 and len(coordinators[row - 1].get_last_name()) and \
                        len(updated_first_name) != 0 and len(updated_last_name) != 0:
                    self.__employees_data.modify_employee(coordinators[row - 1].get_first_name(),
                                                          coordinators[row - 1].get_last_name(),
                                                          updated_first_name, updated_last_name, False)
        self.update_coordinators_table()

    def add_new_coordinator(self):
        first_name_field = self.__administrator_view.get_first_name_field()
        last_name_field = self.__administrator_view.get_last_name_field()
        first_name = first_name_field.get()
        last_name = last_name_field.get()
        if len(first_name) != 0 and len(last_name) != 0:
            exists = self.__employees_data.search_employee(first_name, last_name)
            if not exists:
                self.__employees_data.add_employee(first_name, last_name, False)
        self.update_coordinators_table()

    def update_coordinators_table(self):
        coordinators = self.__employees_data.get_coordinators()
        number_of_coordinators = len(coordinators)
        coordinators_table = self.__administrator_view.get_coordinators_table()
        for row in range(1, len(coordinators_table) - 1):
            for column in range(1, len(coordinators_table[row])):
                if row <= number_of_coordinators:
                    if column == 1:
                        coordinators_table[row][column].delete(0, 'end')
                        coordinators_table[row][column].insert(0, coordinators[row - 1].get_first_name())
                    elif column == 2:
                        coordinators_table[row][column].delete(0, 'end')
                        coordinators_table[row][column].insert(0, coordinators[row - 1].get_last_name())
                if row >= number_of_coordinators + 1:
                    if column == 1:
                        coordinators_table[row][column].delete(0, 'end')
                    elif column == 2:
                        coordinators_table[row][column].delete(0, 'end')

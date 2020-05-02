from tkinter import *
from tkinter.ttk import Notebook
import tkinter.ttk as ttk


class AdmnistratorView:
    def __init__(self, base_view):
        self.__no_of_employees = 13
        self.__no_of_coordinators = 13
        self.__coordinators_table = [[None for _ in range(3)] for _ in range(self.__no_of_coordinators + 1)]
        self.__employees_table = [[None for _ in range(5)] for _ in range(self.__no_of_employees + 1)]

        self.__administrator_window = base_view
        self.__administrator_window.wm_state('zoomed')
        self.__administrator_window.config(bg="#F0F0F0")
        self.__administrator_window.overrideredirect(True)
        self.__administrator_window.attributes('-topmost', True)
        self.__administrator_window.attributes("-fullscreen", False)
        self.__administrator_frame = Frame(self.__administrator_window, bg="#64b167")

        s = ttk.Style()
        s.configure('TNotebook.Tab', font=('fixedsys', '18'))

        self.__logo_img = PhotoImage(file="../images/administrator.png")
        self.__logo_label = Label(self.__administrator_frame)
        self.__logo_label.grid(row=0, column=0, sticky="w", padx=(24, 24))
        self.__logo_label.config(image=self.__logo_img)

        self.__name_label = Label(self.__administrator_frame, text="Full name", bg="#64b167")
        self.__name_label.grid(row=1, column=0, sticky="w", padx=(24, 0), pady=(24, 0))
        self.__name_label.config(font=("fixedsys", "18"))

        self.__acctual_name_label = Label(self.__administrator_frame, text="........", bg="#64b167")
        self.__acctual_name_label.grid(row=2, column=0, sticky="w", padx=(24, 0), pady=(5, 0))
        self.__acctual_name_label.config(font=("fixedsys", "18"))

        self.__password_label = Label(self.__administrator_frame, text="Old password", bg="#64b167")
        self.__password_label.grid(row=3, column=0, stick="w", padx=(24, 0), pady=(24, 0))
        self.__password_label.config(font=("fixedsys", "18"))

        self.__password_text_field = Entry(self.__administrator_frame)
        self.__password_text_field.grid(row=4, column=0, stick="we", padx=(12, 12), pady=(5, 0))
        self.__password_text_field.config(font=("fixedsys", "16"))

        self.__password_label = Label(self.__administrator_frame, text="New password", bg="#64b167")
        self.__password_label.grid(row=5, column=0, stick="w", padx=(24, 0), pady=(24, 0))
        self.__password_label.config(font=("fixedsys", "18"))

        self.__new_password_text_field = Entry(self.__administrator_frame)
        self.__new_password_text_field.grid(row=6, column=0, stick="we", padx=(12, 12), pady=(5, 0))
        self.__new_password_text_field.config(font=("fixedsys", "16"))

        self.__password_button = Button(self.__administrator_frame, width=32, height=3, relief=RIDGE,
                                        bd=2, cursor="hand2", text="Change password", bg="#64b167")
        self.__password_button.grid(row=7, column=0, stick="we", padx=(24, 24), pady=(244, 0))
        self.__password_button.config(font=('fixedsys', 12))

        self.__administrator_frame.pack(side="right", fill="y")

        self.__pages = Notebook(self.__administrator_window, width=200, height=1048)
        self.__page1 = Frame(self.__pages)

        self.__page1_table = Frame(self.__page1, bg="#64b167")

        self.generate_coordinators_table()

        self.__add_new_coordinator_button = Button(self.__page1_table, width=32, height=3, relief=RIDGE,
                                                   bd=2, cursor="hand2", text="Add new coordinator", bg="#E4EAF6")
        self.__add_new_coordinator_button.config(font=('fixedsys', 12))
        self.__add_new_coordinator_button.grid(row=self.__no_of_coordinators, column=0, sticky="nsew", padx=1, pady=1)

        self.__update_coordinator_button = Button(self.__page1_table, width=32, height=3, relief=RIDGE,
                                                  bd=2, cursor="hand2", text="Update coordinator", bg="#E4EAF6")
        self.__update_coordinator_button.config(font=('fixedsys', 12))
        self.__update_coordinator_button.grid(row=self.__no_of_coordinators, column=1, sticky="nsew", padx=1, pady=1)

        self.__delete_coordinator_button = Button(self.__page1_table, width=32, height=3, relief=RIDGE,
                                                  bd=2, cursor="hand2", text="Delete coordinator", bg="#E4EAF6")
        self.__delete_coordinator_button.config(font=('fixedsys', 12))
        self.__delete_coordinator_button.grid(row=self.__no_of_coordinators, column=2, sticky="nsew", padx=1, pady=1)

        self.__page1_table.pack(fill="x", pady=(0, 0))

        self.__page1_panel = Frame(self.__page1)

        self.__first_name_employee_label = Label(self.__page1_panel, text="First name", bg="#64b167")
        self.__first_name_employee_label.config(font=("fixedsys", "18"))
        self.__first_name_employee_label.pack(padx=(460, 2), pady=(32, 0))

        self.__first_name_field = Entry(self.__page1_panel)
        self.__first_name_field.config(font=("fixedsys", "16"))
        self.__first_name_field.pack(padx=(494, 0), pady=(5, 0))

        self.__last_name_employee_label = Label(self.__page1_panel, text="Last name", bg="#64b167")
        self.__last_name_employee_label.config(font=("fixedsys", "18"))
        self.__last_name_employee_label.pack(padx=(440, 0), pady=(40, 0))

        self.__last_name_field = Entry(self.__page1_panel)
        self.__last_name_field.config(font=("fixedsys", "16"))
        self.__last_name_field.pack(padx=(494, 0), pady=(5, 0))

        self.__number_label = Label(self.__page1_panel, text="Number", bg="#64b167")
        self.__number_label.config(font=("fixedsys", "18"))
        self.__number_label.pack(padx=(394, 0), pady=(40, 0))

        self.__number_of_coordinator = Entry(self.__page1_panel)
        self.__number_of_coordinator.config(font=("fixedsys", "16"))
        self.__number_of_coordinator.pack(padx=(494, 0), pady=(5, 0))

        self.__page1_panel.pack()

        self.__page1.pack(fill=BOTH)

        self.__pages.add(self.__page1, text=" Coordinators ")

        self.__page2 = Frame(self.__pages)

        self.__page2_table = Frame(self.__page2, bg="#64b167")

        self.generate_employees_table()

        self.__add_new_employee_button = Button(self.__page2_table, width=32, height=3, relief=RIDGE,
                                                bd=2, cursor="hand2", text="Add new employee", bg="#E4EAF6")
        self.__add_new_employee_button.config(font=('fixedsys', 12))
        self.__add_new_employee_button.grid(row=self.__no_of_employees, column=2, sticky="nsew", padx=1, pady=1)

        self.__update_employee_button = Button(self.__page2_table, width=32, height=3, relief=RIDGE,
                                               bd=2, cursor="hand2", text="Update employee", bg="#E4EAF6")
        self.__update_employee_button.config(font=('fixedsys', 12))
        self.__update_employee_button.grid(row=self.__no_of_employees, column=3, sticky="nsew", padx=1, pady=1)

        self.__delete_employee_button = Button(self.__page2_table, width=32, height=3, relief=RIDGE,
                                               bd=2, cursor="hand2", text="Delete employee", bg="#E4EAF6")
        self.__delete_employee_button.config(font=('fixedsys', 12))
        self.__delete_employee_button.grid(row=self.__no_of_employees, column=4, sticky="nsew", padx=1, pady=1)

        self.__page2_table.pack(fill="x", pady=(0, 0))

        self.__page2_panel = Frame(self.__page2)

        self.__first_name_employee_label = Label(self.__page2_panel, text="First name", bg="#64b167")
        self.__first_name_employee_label.config(font=("fixedsys", "18"))
        self.__first_name_employee_label.pack(padx=(788, 0), pady=(16, 0))

        self.__first_name_employe_field = Entry(self.__page2_panel)
        self.__first_name_employe_field.config(font=("fixedsys", "16"))
        self.__first_name_employe_field.pack(padx=(828, 0), pady=(5, 0))

        self.__last_name_employee_label = Label(self.__page2_panel, text="Last Name", bg="#64b167")
        self.__last_name_employee_label.config(font=("fixedsys", "18"))
        self.__last_name_employee_label.pack(padx=(778, 2), pady=(15, 0))

        self.__last_name_employe_field = Entry(self.__page2_panel)
        self.__last_name_employe_field.config(font=("fixedsys", "16"))
        self.__last_name_employe_field.pack(padx=(828, 0), pady=(5, 0))

        self.__coordinator_name_label = Label(self.__page2_panel, text="Coordinator", bg="#64b167")
        self.__coordinator_name_label.config(font=("fixedsys", "18"))
        self.__coordinator_name_label.pack(padx=(808, 2), pady=(15, 0))

        self.__coordinator_name_field = Entry(self.__page2_panel)
        self.__coordinator_name_field.config(font=("fixedsys", "16"))
        self.__coordinator_name_field.pack(padx=(828, 0), pady=(5, 0))

        self.__employee_number_label = Label(self.__page2_panel, text="Number", bg="#64b167")
        self.__employee_number_label.config(font=("fixedsys", "18"))
        self.__employee_number_label.pack(padx=(728, 2), pady=(15, 0))

        self.__employee_number_field = Entry(self.__page2_panel)
        self.__employee_number_field.config(font=("fixedsys", "16"))
        self.__employee_number_field.pack(padx=(828, 0), pady=(5, 0))

        self.__page2_panel.pack(fill=BOTH)

        self.__page2.pack(fill=BOTH)

        self.__pages.add(self.__page2, text=" Employees ")

        self.__pages.pack(fill=BOTH)

    def generate_coordinators_table(self):
        for row in range(self.__no_of_coordinators):
            for column in range(3):
                try:
                    if row == 0:
                        if column == 0:
                            self.__coordinators_table[row][column] = Label(self.__page1_table, text="No", bg="white",
                                                                           fg="black", padx=3, pady=3)
                        if column == 1:
                            self.__coordinators_table[row][column] = Label(self.__page1_table, text="First name",
                                                                           bg="white",
                                                                           fg="black", padx=3, pady=3)
                        elif column == 2:
                            self.__coordinators_table[row][column] = Label(self.__page1_table, text="Last name",
                                                                           bg="white", fg="black", padx=3, pady=3)
                        self.__coordinators_table[row][column].config(font=('fixedsys', 15), bg="#64b167")
                        self.__coordinators_table[row][column].grid(row=row, column=column, sticky="nsew", padx=1,
                                                                    pady=1)
                        self.__page1_table.grid_columnconfigure(column, weight=22)
                    else:
                        if column == 0:
                            self.__coordinators_table[row][column] = Label(self.__page1_table, text=str(row) + ".",
                                                                           bg="white", fg="black", padx=0, pady=3)
                            self.__coordinators_table[row][column].grid(row=row, column=column, sticky="nsew", padx=1,
                                                                        pady=1)
                            self.__coordinators_table[row][column].config(font=('fixedsys', 15))
                            self.__page1_table.grid_columnconfigure(column, weight=1)
                        else:
                            self.__coordinators_table[row][column] = Entry(self.__page1_table, text="Data " + str(row) +
                                                                                                    " " + str(column))
                            self.__coordinators_table[row][column].grid(row=row, column=column, sticky="nsew", padx=1,
                                                                        pady=1)
                            self.__coordinators_table[row][column].config(font=('fixedsys', 15))
                            self.__page1_table.grid_columnconfigure(column, weight=22)
                except TypeError:
                    pass

    def generate_employees_table(self):
        for row in range(self.__no_of_employees):
            for column in range(5):
                try:
                    if row == 0:
                        if column == 0:
                            self.__employees_table[row][column] = Label(self.__page2_table, text="No", bg="white",
                                                                        fg="black", padx=3, pady=3)
                        elif column == 1:
                            self.__employees_table[row][column] = Label(self.__page2_table, text="First name",
                                                                        bg="white", fg="black", padx=3, pady=3)
                        elif column == 2:
                            self.__employees_table[row][column] = Label(self.__page2_table, text="Last name",
                                                                        bg="white", fg="black", padx=3, pady=3)
                        elif column == 3:
                            self.__employees_table[row][column] = Label(self.__page2_table, text="Location", bg="white",
                                                                        fg="black", padx=3, pady=3)
                        elif column == 4:
                            self.__employees_table[row][column] = Label(self.__page2_table, text="Coordinator",
                                                                        bg="white", fg="black", padx=3, pady=3)
                        self.__employees_table[row][column].config(font=('fixedsys', 15), bg="#64b167")
                        self.__employees_table[row][column].grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        self.__page2_table.grid_columnconfigure(column, weight=1)
                    else:
                        if column == 0:
                            self.__employees_table[row][column] = Label(self.__page2_table, text=str(row) + ".",
                                                                        bg="white", fg="black", padx=3, pady=3)
                            self.__employees_table[row][column].grid(row=row, column=column, sticky="nsew", padx=1,
                                                                     pady=1)
                            self.__employees_table[row][column].config(font=('fixedsys', 15))
                            self.__page2_table.grid_columnconfigure(column, weight=1)
                        elif column == 3:
                            self.__employees_table[row][column] = Label(self.__page2_table, text="", bg="white",
                                                                        fg="black", padx=3, pady=3)
                            self.__employees_table[row][column].grid(row=row, column=column, sticky="nsew", padx=1,
                                                                     pady=1)
                            self.__employees_table[row][column].config(font=('fixedsys', 15))
                            self.__page2_table.grid_columnconfigure(column, weight=1)
                        else:
                            self.__employees_table[row][column] = Entry(self.__page2_table, text="")
                            self.__employees_table[row][column].grid(row=row, column=column, sticky="nsew", padx=1,
                                                                     pady=1)
                            self.__employees_table[row][column].config(font=('fixedsys', 15))
                            self.__page2_table.grid_columnconfigure(column, weight=1)
                except TypeError:
                    pass

    def get_administrator_window(self):
        return self.__administrator_window

    def get_acctual_administrator_label(self):
        return self.__acctual_name_label

    def get_change_admin_password_button(self):
        return self.__password_button

    def get_password_field(self):
        return self.__password_text_field

    def get_new_password_field(self):
        return self.__new_password_text_field

    def get_add_coordinator_button(self):
        return self.__add_new_coordinator_button

    def get_update_coordinator_button(self):
        return self.__update_coordinator_button

    def get_number_of_coordinator_field(self):
        return self.__number_of_coordinator

    def get_delete_coordinator_button(self):
        return self.__delete_coordinator_button

    def get_first_name_field(self):
        return self.__first_name_field

    def get_last_name_field(self):
        return self.__last_name_field

    def get_coordinators_table(self):
        return self.__coordinators_table

    def get_employees_table(self):
        return self.__employees_table

    def get_add_employee_button(self):
        return self.__add_new_employee_button

    def get_update_employee_button(self):
        return self.__update_employee_button

    def get_delete_employee_button(self):
        return self.__delete_employee_button

    def get_employee_first_name_field(self):
        return self.__first_name_employe_field

    def get_employee_last_name_field(self):
        return self.__last_name_employe_field

    def get_coordinator_for_employee(self):
        return self.__coordinator_name_field

    def get_employee_number(self):
        return self.__employee_number_field

    def get_tabs(self):
        return self.__pages

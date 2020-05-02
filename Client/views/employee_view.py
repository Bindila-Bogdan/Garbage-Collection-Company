from tkinter import *
import time


class EmployeeView:
    def __init__(self, base_view, route_controller):
        self.__route_controll = route_controller
        self.__route_controll.generate_map()
        self.__employee_window = base_view
        self.__employee_window.attributes("-fullscreen", False)
        self.__employee_window.wm_state('zoomed')
        self.__employee_window.config(bg="#F0F0F0")
        self.__employee_window.overrideredirect(True)
        self.__employee_window.attributes('-topmost', True)
        self.__employee_frame = Frame(self.__employee_window, bg="#64b167")

        self.__map_frame = Frame(self.__employee_window)
        self.__map_img = PhotoImage(file="../views/plot.png")
        self.__map_label = Canvas(self.__map_frame, width=1500, height=400)
        self.__map_label.create_image(0, 0, anchor=NW, image=self.__map_img)
        self.__map_label.pack(expand=YES, fill=BOTH)
        self.__map_frame.pack(side="left", fill="both", padx=(60, 0), pady=(16, 0))

        self.__logo_img = PhotoImage(file="../images/employee.png")
        self.__logo_label = Label(self.__employee_frame)
        self.__logo_label.grid(row=0, column=0, sticky="w", padx=(48, 48))
        self.__logo_label.config(image=self.__logo_img)

        self.__name_label = Label(self.__employee_frame, text="Full name", bg="#64b167")
        self.__name_label.grid(row=1, column=0, sticky="w", padx=(24, 0), pady=(48, 0))
        self.__name_label.config(font=("fixedsys", "18"))

        self.__acctual_name_label = Label(self.__employee_frame, text="........", bg="#64b167")
        self.__acctual_name_label.grid(row=2, column=0, sticky="w", padx=(24, 0), pady=(5, 0))
        self.__acctual_name_label.config(font=("fixedsys", "18"))

        self.__location_label = Label(self.__employee_frame, text="Location", bg="#64b167")
        self.__location_label.grid(row=3, column=0, stick="w", padx=(24, 0), pady=(24, 0))
        self.__location_label.config(font=("fixedsys", "18"))
        self.__acctual_location_label = Label(self.__employee_frame, text="........", bg="#64b167")
        self.__acctual_location_label.grid(row=4, column=0, stick="w", padx=(24, 0), pady=(5, 0))
        self.__acctual_location_label.config(font=("fixedsys", "18"))

        self.__coordinator_label = Label(self.__employee_frame, text="Coordinator", bg="#64b167")
        self.__coordinator_label.grid(row=5, column=0, stick="w", padx=(24, 0), pady=(24, 0))
        self.__coordinator_label.config(font=("fixedsys", "18"))
        self.__acctual__coordinator_label = Label(self.__employee_frame, text="........", bg="#64b167")
        self.__acctual__coordinator_label.grid(row=6, column=0, stick="w", padx=(24, 0), pady=(5, 0))
        self.__acctual__coordinator_label.config(font=("fixedsys", "18"))

        self.__password_label = Label(self.__employee_frame, text="Old password", bg="#64b167")
        self.__password_label.grid(row=7, column=0, stick="w", padx=(24, 0), pady=(24, 0))
        self.__password_label.config(font=("fixedsys", "18"))
        self.__password_text_field = Entry(self.__employee_frame)
        self.__password_text_field.grid(row=8, column=0, stick="we", padx=(12, 12), pady=(5, 0))
        self.__password_text_field.config(font=("fixedsys", "18"))

        self.__password_label = Label(self.__employee_frame, text="New password", bg="#64b167")
        self.__password_label.grid(row=9, column=0, stick="w", padx=(24, 0), pady=(24, 0))
        self.__password_label.config(font=("fixedsys", "18"))
        self.__new_password_text_field = Entry(self.__employee_frame)
        self.__new_password_text_field.grid(row=10, column=0, stick="we", padx=(12, 12), pady=(5, 0))
        self.__new_password_text_field.config(font=("fixedsys", "18"))

        self.__password_button = Button(self.__employee_frame, height=3, relief=RIDGE,
                                        bd=2, cursor="hand2", text="Change password", bg="#64b167")
        self.__password_button.grid(row=11, column=0, stick="we", padx=(24, 24), pady=(96, 0))
        self.__password_button.config(font=('fixedsys', 14))

        self.__route_button = Button(self.__employee_frame, height=3, relief=RIDGE,
                                     bd=2, cursor="hand2", text="Generate route", bg="#64b167")
        self.__route_button.grid(row=12, column=0, stick="we", padx=(24, 24), pady=(24, 0))
        self.__route_button.config(font=('fixedsys', 14))

        self.__employee_frame.pack(side="right", fill="y")

    def plot_route(self, number_of_nodes):
        for i in range(number_of_nodes):
            self.__route_controll.generate_route()
            time.sleep(0.1)
            try:
                self.__map_img = PhotoImage(file="../views/plot.png")
                self.__map_label.create_image(0, 0, anchor=NW, image=self.__map_img)
                self.__map_label.pack(expand=YES, fill=BOTH)
                self.__map_frame.pack(side="left", fill="both", padx=(60, 0))
            except RuntimeError:
                pass
            self.__employee_window.mainloop()

    def get_employee_window(self):
        return self.__employee_window

    def get_generate_route_button(self):
        return self.__route_button

    def get_change_password_button(self):
        return self.__password_button

    def get_acctual_location_label(self):
        return self.__acctual_location_label

    def get_acctual_name_label(self):
        return self.__acctual_name_label

    def get_acctual_coordinator_label(self):
        return self.__acctual__coordinator_label

    def get_password_field(self):
        return self.__password_text_field

    def get_new_password_field(self):
        return self.__new_password_text_field

    def get_route_controll(self):
        return self.__route_controll

    def get_map_label(self):
        return self.__map_label

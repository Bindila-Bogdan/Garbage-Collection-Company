from tkinter import *
import time
from language_manager.language_observer import LanguageObserver


class EmployeeView(LanguageObserver):
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
        self.__map_label = Canvas(self.__map_frame, width=1450, height=400)
        self.__map_label.create_image(0, 0, anchor=NW, image=self.__map_img)
        self.__map_label.pack(expand=YES, fill=BOTH)
        self.__map_frame.pack(side="left", fill="y", padx=(16, 0), pady=(24, 0))

        self.set_background()

        self.__french_img = PhotoImage(file="../images/french.png")
        self.__french_language_button = Button(self.__employee_frame, width=66, height=44, relief=RIDGE,
                                               bd=2, cursor="hand2", image=self.__french_img, bg="#ffffff")
        self.__french_language_button.grid(row=9, column=0, sticky="w", pady=(0, 5), padx=(8, 8))

        self.__english_img = PhotoImage(file="../images/english.png")
        self.__english_language_button = Button(self.__employee_frame, width=66, height=44, relief=RIDGE,
                                                bd=2, cursor="hand2", image=self.__english_img, bg="#ffffff")
        self.__english_language_button.grid(row=11, column=0, sticky="w", pady=(5, 5), padx=(8, 8))

        self.__romanian_img = PhotoImage(file="../images/romanian.png")
        self.__romanian_language_button = Button(self.__employee_frame, width=66, height=44, relief=RIDGE,
                                                 bd=2, cursor="hand2", image=self.__romanian_img, bg="#ffffff")
        self.__romanian_language_button.grid(row=13, column=0, sticky="w", pady=(5, 5), padx=(8, 8))

        self.__spanish_img = PhotoImage(file="../images/spanish.png")
        self.__spanish_language_button = Button(self.__employee_frame, width=66, height=44, relief=RIDGE,
                                                bd=2, cursor="hand2", image=self.__spanish_img, bg="#ffffff")
        self.__spanish_language_button.grid(row=14, column=0, sticky="w", pady=(5, 5), padx=(8, 8))

        self.__logo_img = PhotoImage(file="../images/employee.png")
        self.__logo_label = Label(self.__employee_frame)
        self.__logo_label.grid(row=0, column=1, sticky="we", padx=(48, 48))
        self.__logo_label.config(image=self.__logo_img)

        self.__name_label = Label(self.__employee_frame, text="Full name", bg="#64b167")
        self.__name_label.grid(row=1, column=1, sticky="w", padx=(16, 0), pady=(48, 0))
        self.__name_label.config(font=("fixedsys", "18"))

        self.__acctual_name_label = Label(self.__employee_frame, text="........", bg="#64b167")
        self.__acctual_name_label.grid(row=2, column=1, sticky="w", padx=(16, 0), pady=(5, 0))
        self.__acctual_name_label.config(font=("fixedsys", "18"))

        self.__location_label = Label(self.__employee_frame, text="Location", bg="#64b167")
        self.__location_label.grid(row=3, column=1, stick="w", padx=(16, 0), pady=(24, 0))
        self.__location_label.config(font=("fixedsys", "18"))
        self.__acctual_location_label = Label(self.__employee_frame, text="........", bg="#64b167")
        self.__acctual_location_label.grid(row=4, column=1, stick="w", padx=(16, 0), pady=(5, 0))
        self.__acctual_location_label.config(font=("fixedsys", "18"))

        self.__coordinator_label = Label(self.__employee_frame, text="Coordinator", bg="#64b167")
        self.__coordinator_label.grid(row=5, column=1, stick="w", padx=(16, 0), pady=(24, 0))
        self.__coordinator_label.config(font=("fixedsys", "18"))
        self.__acctual__coordinator_label = Label(self.__employee_frame, text="........", bg="#64b167")
        self.__acctual__coordinator_label.grid(row=6, column=1, stick="w", padx=(16, 0), pady=(5, 0))
        self.__acctual__coordinator_label.config(font=("fixedsys", "18"))

        self.__old_password_label = Label(self.__employee_frame, text="Old password", bg="#64b167")
        self.__old_password_label.grid(row=7, column=1, stick="w", padx=(16, 0), pady=(24, 0))
        self.__old_password_label.config(font=("fixedsys", "18"))
        self.__password_text_field = Entry(self.__employee_frame)
        self.__password_text_field.grid(row=8, column=1, stick="we", padx=(16, 12), pady=(5, 0))
        self.__password_text_field.config(font=("fixedsys", "18"))

        self.__new_password_label = Label(self.__employee_frame, text="New password", bg="#64b167")
        self.__new_password_label.grid(row=9, column=1, stick="w", padx=(16, 0), pady=(24, 0))
        self.__new_password_label.config(font=("fixedsys", "18"))
        self.__new_password_text_field = Entry(self.__employee_frame)
        self.__new_password_text_field.grid(row=10, column=1, stick="we", padx=(16, 12), pady=(5, 12))
        self.__new_password_text_field.config(font=("fixedsys", "18"))

        self.__password_button = Button(self.__employee_frame, height=3, relief=RIDGE,
                                        bd=2, cursor="hand2", text="Change password", bg="#64b167")
        self.__password_button.grid(row=13, column=1, stick="we", padx=(24, 24), pady=(12, 0))
        self.__password_button.config(font=('fixedsys', 14))

        self.__route_button = Button(self.__employee_frame, height=3, relief=RIDGE,
                                     bd=2, cursor="hand2", text="Generate route", bg="#64b167")
        self.__route_button.grid(row=14, column=1, stick="we", padx=(24, 24), pady=(12, 48))
        self.__route_button.config(font=('fixedsys', 14))

        self.__employee_frame.pack(side="right", fill="y")

    def set_background(self):
        for i in range(0, 15):
            __dummy = Label(self.__employee_frame, bg="#F0F0F0")
            __dummy.grid(row=i, column=0, sticky="wesn")

    def plot_route(self, number_of_nodes):
        for i in range(number_of_nodes):
            self.__route_controll.generate_route()
            time.sleep(0.1)
            try:
                self.__map_img = PhotoImage(file="../views/plot.png")
                self.__map_label.create_image(0, 0, anchor=NW, image=self.__map_img)
                self.__map_label.pack(expand=YES, fill=BOTH)
                self.__map_frame.pack(side="left", fill="both", padx=(16, 0))
            except RuntimeError:
                pass
            self.__employee_window.mainloop()

    def update(self, dictionary, index):
        name_label_text = self.__name_label['text']
        location_label_text = self.__location_label['text']
        coordinator_label_text = self.__coordinator_label['text']
        old_password_label_text = self.__old_password_label['text']
        new_password_label_text = self.__new_password_label['text']
        change_password_button_text = self.__password_button['text']
        generate_route_button_text = self.__route_button['text']
        print(change_password_button_text)
        for (_, value) in dictionary.items():
            new_text = value[index]
            if name_label_text in value:
                self.__name_label.configure(text=new_text)
            elif location_label_text in value:
                self.__location_label.configure(text=new_text)
            elif coordinator_label_text in value:
                self.__coordinator_label.configure(text=new_text)
            elif old_password_label_text in value:
                self.__old_password_label.configure(text=new_text)
            elif new_password_label_text in value:
                self.__new_password_label.configure(text=new_text)
            elif change_password_button_text in value:
                self.__password_button.configure(text=new_text)
            elif generate_route_button_text in value:
                self.__route_button.configure(text=new_text)

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

    def get_french_language_button(self):
        return self.__french_language_button

    def get_english_language_button(self):
        return self.__english_language_button

    def get_romanian_language_button(self):
        return self.__romanian_language_button

    def get_spanish_language_button(self):
        return self.__spanish_language_button

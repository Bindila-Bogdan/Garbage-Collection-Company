from tkinter import *
from tkinter.ttk import Notebook
import tkinter.ttk as ttk
import time
from language_manager.language_observer import LanguageObserver


class CoordinatorView(LanguageObserver):
    def __init__(self, base_view, route_controller):
        self.__route_controll = route_controller
        self.__route_controll.generate_map()
        self.__no_of_employees = 13
        self.__employees_table = [[None for _ in range(4)] for _ in range(self.__no_of_employees + 1)]
        self.__locations_table = [[None for _ in range(5)] for _ in range(self.__no_of_employees + 1)]

        self.__coordinator_window = base_view
        self.__coordinator_window.wm_state('zoomed')
        self.__coordinator_window.config(bg="#F0F0F0")
        self.__coordinator_window.overrideredirect(True)
        self.__coordinator_window.attributes('-topmost', True)
        self.__coordinator_window.attributes("-fullscreen", False)
        self.__coordinator_frame = Frame(self.__coordinator_window, bg="#64b167")

        s = ttk.Style()
        s.configure('TNotebook.Tab', font=('fixedsys', '18'))

        self.__pages = Notebook(self.__coordinator_window, width=200, height=1048)
        self.__page1 = Frame(self.__pages)

        self.set_background()

        self.__map_frame = Frame(self.__page1)
        self.__map_img = PhotoImage(file="../views/plot.png")
        self.__map_label = Canvas(self.__map_frame, width=1500, height=400)
        self.__map_label.create_image(0, 1, anchor=NW, image=self.__map_img)
        self.__map_frame.pack(side="left", fill="y", padx=(60, 0))

        self.__french_img = PhotoImage(file="../images/french.png")
        self.__french_language_button = Button(self.__coordinator_frame, width=66, height=44, relief=RIDGE,
                                               bd=2, cursor="hand2", image=self.__french_img, bg="#ffffff")
        self.__french_language_button.grid(row=8, column=0, sticky="w", pady=(16, 0), padx=(8, 8))

        self.__english_img = PhotoImage(file="../images/english.png")
        self.__english_language_button = Button(self.__coordinator_frame, width=66, height=44, relief=RIDGE,
                                                bd=2, cursor="hand2", image=self.__english_img, bg="#ffffff")
        self.__english_language_button.grid(row=9, column=0, sticky="w", pady=(0, 0), padx=(8, 8))

        self.__romanian_img = PhotoImage(file="../images/romanian.png")
        self.__romanian_language_button = Button(self.__coordinator_frame, width=66, height=44, relief=RIDGE,
                                                 bd=2, cursor="hand2", image=self.__romanian_img, bg="#ffffff")
        self.__romanian_language_button.grid(row=10, column=0, sticky="w", pady=(0, 0), padx=(8, 8))

        self.__spanish_img = PhotoImage(file="../images/spanish.png")
        self.__spanish_language_button = Button(self.__coordinator_frame, width=66, height=44, relief=RIDGE,
                                                bd=2, cursor="hand2", image=self.__spanish_img, bg="#ffffff")
        self.__spanish_language_button.grid(row=11, column=0, sticky="w", pady=(0, 16), padx=(8, 8))

        self.__logo_img = PhotoImage(file="../images/coordinator.png")
        self.__logo_label = Label(self.__coordinator_frame)
        self.__logo_label.grid(row=0, column=1, sticky="w", padx=(48, 48))
        self.__logo_label.config(image=self.__logo_img)

        self.__name_label = Label(self.__coordinator_frame, text="Full name", bg="#64b167")
        self.__name_label.grid(row=1, column=1, sticky="w", padx=(12, 0), pady=(24, 0))
        self.__name_label.config(font=("fixedsys", "18"))

        self.__acctual_name_label = Label(self.__coordinator_frame, text="........", bg="#64b167")
        self.__acctual_name_label.grid(row=2, column=1, sticky="w", padx=(12, 0), pady=(5, 0))
        self.__acctual_name_label.config(font=("fixedsys", "18"))

        self.__old_password_label = Label(self.__coordinator_frame, text="Old password", bg="#64b167")
        self.__old_password_label.grid(row=3, column=1, stick="w", padx=(12, 0), pady=(24, 0))
        self.__old_password_label.config(font=("fixedsys", "18"))
        self.__password_text_field = Entry(self.__coordinator_frame)
        self.__password_text_field.grid(row=4, column=1, stick="we", padx=(12, 12), pady=(5, 0))
        self.__password_text_field.config(font=("fixedsys", "18"))

        self.__new_password_label = Label(self.__coordinator_frame, text="New password", bg="#64b167")
        self.__new_password_label.grid(row=5, column=1, stick="w", padx=(12, 0), pady=(24, 0))
        self.__new_password_label.config(font=("fixedsys", "18"))
        self.__new_password_text_field = Entry(self.__coordinator_frame)
        self.__new_password_text_field.grid(row=6, column=1, stick="we", padx=(12, 12), pady=(5, 0))
        self.__new_password_text_field.config(font=("fixedsys", "18"))

        self.__password_button = Button(self.__coordinator_frame, height=3, relief=RIDGE,
                                        bd=2, cursor="hand2", text="Change password", bg="#64b167")
        self.__password_button.grid(row=7, column=1, stick="we", padx=(24, 24), pady=(24, 0))
        self.__password_button.config(font=('fixedsys', 14))

        self.__route_button = Button(self.__coordinator_frame, height=3, relief=RIDGE,
                                     bd=2, cursor="hand2", text="Generate route", bg="#64b167")
        self.__route_button.grid(row=8, column=1, stick="we", padx=(24, 24), pady=(24, 0))
        self.__route_button.config(font=('fixedsys', 14))

        self.__csv_button = Button(self.__coordinator_frame, height=3, relief=RIDGE,
                                   bd=2, cursor="hand2", text="CSV Report", bg="#64b167")
        self.__csv_button.grid(row=9, column=1, stick="we", padx=(24, 24), pady=(24, 0))
        self.__csv_button.config(font=('fixedsys', 14))

        self.__json_button = Button(self.__coordinator_frame, height=3, relief=RIDGE,
                                    bd=2, cursor="hand2", text="JSON Report", bg="#64b167")
        self.__json_button.grid(row=10, column=1, stick="we", padx=(24, 24), pady=(24, 0))
        self.__json_button.config(font=('fixedsys', 14))

        self.__xml_button = Button(self.__coordinator_frame, height=3, relief=RIDGE,
                                   bd=2, cursor="hand2", text="XML Report", bg="#64b167")
        self.__xml_button.grid(row=11, column=1, stick="we", padx=(24, 24), pady=(24, 36))
        self.__xml_button.config(font=('fixedsys', 14))

        self.__coordinator_frame.pack(side="right", fill="y")

        self.__page1.pack(fill=BOTH)
        self.__pages.add(self.__page1, text=" Map ")

        self.__page2 = Frame(self.__pages)

        self.__page2_table = Frame(self.__page2, bg="#64b167")

        self.generate_employees_table()

        self.__page2_table.pack(fill="x", pady=(0, 256))

        self.__page2_panel = Frame(self.__page2)

        self.__update_employees_locations_button = Button(self.__page2_panel, width=64, height=3, relief=RIDGE,
                                                          bd=2, cursor="hand2", text="Update locations assigned",
                                                          bg="#FF8709")
        self.__update_employees_locations_button.config(font=('fixedsys', 16))
        self.__update_employees_locations_button.pack(padx=(1000, 15), pady=(270, 0))

        self.__page2_panel.pack()

        self.__page2.pack(fill=BOTH)
        self.__pages.add(self.__page2, text=" Coordinated Employees ")

        self.__page3 = Frame(self.__pages)

        self.__page3_table = Frame(self.__page3, bg="#64b167")

        self.generate_locations_table()

        self.__add_new_location_button = Button(self.__page3_table, width=32, height=3, relief=RIDGE,
                                                bd=2, cursor="hand2", text="Add new location", bg="#FF8709")
        self.__add_new_location_button.config(font=('fixedsys', 16))
        self.__add_new_location_button.grid(row=self.__no_of_employees, column=2, sticky="nsew", padx=1, pady=1)

        self.__update_locations_button = Button(self.__page3_table, width=32, height=3, relief=RIDGE,
                                                bd=2, cursor="hand2", text="Update locations", bg="#FF8709")
        self.__update_locations_button.config(font=('fixedsys', 16))
        self.__update_locations_button.grid(row=self.__no_of_employees, column=3, sticky="nsew", padx=1, pady=1)

        self.__delete_location_button = Button(self.__page3_table, width=32, height=3, relief=RIDGE,
                                               bd=2, cursor="hand2", text="Delete location", bg="#FF8709")
        self.__delete_location_button.config(font=('fixedsys', 16))
        self.__delete_location_button.grid(row=self.__no_of_employees, column=4, sticky="nsew", padx=1, pady=1)

        self.__page3_table.pack(fill="x", pady=(0, 0))

        self.__page3_panel = Frame(self.__page3)

        self.__new_location_name = Label(self.__page3_panel, text="New location name", bg="#64b167")
        self.__new_location_name.config(font=("fixedsys", "18"))
        self.__new_location_name.grid(row=0, column=0, stick="w", padx=(674, 24), pady=(24, 0))

        self.__new_location_name_field = Entry(self.__page3_panel)
        self.__new_location_name_field.config(font=("fixedsys", "16"))
        self.__new_location_name_field.grid(row=1, column=0, stick="w", padx=(674, 24), pady=(12, 0))

        self.__ox_coord = Label(self.__page3_panel, text="Ox coordinate", bg="#64b167")
        self.__ox_coord.config(font=("fixedsys", "18"))
        self.__ox_coord.grid(row=2, column=0, stick="w", padx=(674, 24), pady=(24, 0))

        self.__ox_coord_field = Entry(self.__page3_panel)
        self.__ox_coord_field.config(font=("fixedsys", "16"))
        self.__ox_coord_field.grid(row=3, column=0, stick="w", padx=(674, 24), pady=(12, 0))

        self.__oy_coord = Label(self.__page3_panel, text="Oy coordinate", bg="#64b167")
        self.__oy_coord.config(font=("fixedsys", "18"))
        self.__oy_coord.grid(row=4, column=0, stick="w", padx=(674, 24), pady=(24, 0))

        self.__oy_coord_field = Entry(self.__page3_panel)
        self.__oy_coord_field.config(font=("fixedsys", "16"))
        self.__oy_coord_field.grid(row=5, column=0, stick="w", padx=(674, 24), pady=(12, 0))

        self.__location_name = Label(self.__page3_panel, text="Enter location name", bg="#64b167")
        self.__location_name.config(font=("fixedsys", "18"))
        self.__location_name.grid(row=6, column=0, stick="w", padx=(674, 24), pady=(24, 0))

        self.__location_name_field = Entry(self.__page3_panel)
        self.__location_name_field.config(font=("fixedsys", "16"))
        self.__location_name_field.grid(row=7, column=0, stick="w", padx=(674, 24), pady=(12, 0))

        self.__page3_panel.pack(fill=BOTH)

        self.__page3.pack(fill=BOTH)

        self.__page3.pack(fill=BOTH)
        self.__pages.add(self.__page3, text=" Locations ")

        self.__pages.pack(fill=BOTH)

    def set_background(self):
        for i in range(0, 12):
            __dummy = Label(self.__coordinator_frame, bg="#F0F0F0")
            __dummy.grid(row=i, column=0, sticky="wesn")

    def change_image(self):
        try:
            self.__map_img = PhotoImage(file="../views/plot.png")
            self.__map_label.create_image(0, 0, anchor=NW, image=self.__map_img)
            self.__map_label.pack(expand=YES, fill=BOTH)
            self.__map_frame.pack(side="left", fill="both", padx=(60, 0))
        except RuntimeError:
            pass
        self.__coordinator_window.mainloop()

    def generate_employees_table(self):
        for row in range(self.__no_of_employees):
            for column in range(4):
                try:
                    if row == 0:
                        if column == 0:
                            self.__employees_table[row][column] = Label(self.__page2_table, text="No", bg="white",
                                                                        fg="black", padx=3, pady=3)
                        if column == 1:
                            self.__employees_table[row][column] = Label(self.__page2_table, text="First name",
                                                                        bg="white",
                                                                        fg="black", padx=3, pady=3)
                        elif column == 2:
                            self.__employees_table[row][column] = Label(self.__page2_table, text="Last name",
                                                                        bg="white",
                                                                        fg="black", padx=3,
                                                                        pady=3)
                        elif column == 3:
                            self.__employees_table[row][column] = Label(self.__page2_table, text="Location", bg="white",
                                                                        fg="black", padx=3,
                                                                        pady=3)
                        self.__employees_table[row][column].config(font=('fixedsys', 16), bg="#64b167")
                        self.__employees_table[row][column].grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        self.__page2_table.grid_columnconfigure(column, weight=10)
                    else:
                        if column == 0:
                            self.__employees_table[row][column] = Label(self.__page2_table, text=str(row) + ".",
                                                                        bg="white",
                                                                        fg="black", padx=0, pady=3)
                            self.__employees_table[row][column].grid(row=row, column=column, sticky="nsew", padx=1,
                                                                     pady=1)
                            self.__employees_table[row][column].config(font=('fixedsys', 16))
                            self.__page2_table.grid_columnconfigure(column, weight=1)
                        elif column == 1 or column == 2:
                            self.__employees_table[row][column] = Label(self.__page2_table, text="", bg="white",
                                                                        fg="black",
                                                                        padx=3, pady=3)
                            self.__employees_table[row][column].grid(row=row, column=column, sticky="nsew", padx=1,
                                                                     pady=1)
                            self.__employees_table[row][column].config(font=('fixedsys', 16))
                            self.__page2_table.grid_columnconfigure(column, weight=10)
                        elif column == 3:
                            self.__employees_table[row][column] = Entry(self.__page2_table,
                                                                        text="Data " + str(row) + " " + str(column))
                            self.__employees_table[row][column].grid(row=row, column=column, sticky="nsew", padx=1,
                                                                     pady=1)
                            self.__employees_table[row][column].config(font=('fixedsys', 16))
                            self.__page2_table.grid_columnconfigure(column, weight=10)
                except TypeError:
                    pass

    def generate_locations_table(self):
        for row in range(self.__no_of_employees):
            for column in range(5):
                try:
                    if row == 0:
                        if column == 0:
                            self.__locations_table[row][column] = Label(self.__page3_table, text="No", bg="white",
                                                                        fg="black", padx=3, pady=3)
                        if column == 1:
                            self.__locations_table[row][column] = Label(self.__page3_table, text="Location name",
                                                                        bg="white", fg="black", padx=3, pady=3)
                        elif column == 2:
                            self.__locations_table[row][column] = Label(self.__page3_table, text="Employee", bg="white",
                                                                        fg="black", padx=3,
                                                                        pady=3)
                        elif column == 3:
                            self.__locations_table[row][column] = Label(self.__page3_table, text="Ox coord", bg="white",
                                                                        fg="black", padx=3,
                                                                        pady=3)
                        elif column == 4:
                            self.__locations_table[row][column] = Label(self.__page3_table, text="Oy coord", bg="white",
                                                                        fg="black", padx=3,
                                                                        pady=3)
                        self.__locations_table[row][column].config(font=('fixedsys', 16), bg="#64b167")
                        self.__locations_table[row][column].grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                        self.__page3_table.grid_columnconfigure(column, weight=20)
                    else:
                        if column == 0:
                            self.__locations_table[row][column] = Label(self.__page3_table, text=str(row) + ".",
                                                                        bg="white",
                                                                        fg="black", padx=0, pady=3)
                            self.__locations_table[row][column].grid(row=row, column=column, sticky="nsew", padx=1,
                                                                     pady=1)
                            self.__locations_table[row][column].config(font=('fixedsys', 16))
                            self.__page3_table.grid_columnconfigure(column, weight=1)
                        elif column == 1 or column == 2:
                            self.__locations_table[row][column] = Label(self.__page3_table, text="", bg="white",
                                                                        fg="black",
                                                                        padx=3, pady=3)
                            self.__locations_table[row][column].grid(row=row, column=column, sticky="nsew", padx=1,
                                                                     pady=1)
                            self.__locations_table[row][column].config(font=('fixedsys', 16))
                            self.__page3_table.grid_columnconfigure(column, weight=20)
                        else:
                            self.__locations_table[row][column] = Entry(self.__page3_table,
                                                                        text="Data " + str(row) + " " + str(column))
                            self.__locations_table[row][column].grid(row=row, column=column, sticky="nsew", padx=1,
                                                                     pady=1)
                            self.__locations_table[row][column].config(font=('fixedsys', 16))
                            self.__page3_table.grid_columnconfigure(column, weight=20)
                except TypeError:
                    pass

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
            self.__coordinator_window.mainloop()

    def update(self, dictionary, index):
        name_label_text = self.__name_label['text']
        old_password_label_text = self.__old_password_label['text']
        new_password_label_text = self.__new_password_label['text']
        change_password_button_text = self.__password_button['text']
        generate_route_button_text = self.__route_button['text']
        csv_report_button_text = self.__csv_button['text']
        json_report_button_text = self.__json_button['text']
        xml_report_button_text = self.__xml_button['text']
        map_tab_text = self.__pages.tab(0, option='text')
        coordinated_employees_tab_text = self.__pages.tab(1, option='text')
        locations_tab_text = self.__pages.tab(2, option='text')
        update_employees_locations_button_text = self.__update_employees_locations_button['text']
        add_a_new_location_button_text = self.__add_new_location_button['text']
        delete_a_location_button_text = self.__delete_location_button['text']
        update_a_locations_button_text = self.__update_locations_button['text']
        new_location_name_text = self.__new_location_name['text']
        ox_coord_text = self.__ox_coord['text']
        oy_coord_text = self.__oy_coord['text']
        location_name_text = self.__location_name['text']
        emp_table_head_one_text = self.__employees_table[0][0]['text']
        emp_table_head_two_text = self.__employees_table[0][1]['text']
        emp_table_head_three_text = self.__employees_table[0][2]['text']
        emp_table_head_four_text = self.__employees_table[0][3]['text']
        loc_table_head_one_text = self.__locations_table[0][0]['text']
        loc_table_head_two_text = self.__locations_table[0][1]['text']
        loc_table_head_three_text = self.__locations_table[0][2]['text']
        loc_table_head_four_text = self.__locations_table[0][3]['text']
        loc_table_head_five_text = self.__locations_table[0][4]['text']

        for (_, value) in dictionary.items():
            new_text = value[index]
            if name_label_text in value:
                self.__name_label.configure(text=new_text)
            elif old_password_label_text in value:
                self.__old_password_label.configure(text=new_text)
            elif new_password_label_text in value:
                self.__new_password_label.configure(text=new_text)
            elif change_password_button_text in value:
                self.__password_button.configure(text=new_text)
            elif generate_route_button_text in value:
                self.__route_button.configure(text=new_text)
            elif csv_report_button_text in value:
                self.__csv_button.configure(text=new_text)
            elif json_report_button_text in value:
                self.__json_button.configure(text=new_text)
            elif xml_report_button_text in value:
                self.__xml_button.configure(text=new_text)
            elif map_tab_text in value:
                self.__pages.tab(0, text=new_text)
            elif coordinated_employees_tab_text in value:
                self.__pages.tab(1, text=new_text)
            elif locations_tab_text in value:
                self.__pages.tab(2, text=new_text)
            elif update_employees_locations_button_text in value:
                self.__update_employees_locations_button.configure(text=new_text)
            elif add_a_new_location_button_text in value:
                self.__add_new_location_button.configure(text=new_text)
            elif delete_a_location_button_text in value:
                self.__delete_location_button.configure(text=new_text)
            elif update_a_locations_button_text in value:
                self.__update_locations_button.configure(text=new_text)
            elif new_location_name_text in value:
                self.__new_location_name.configure(text=new_text)
            elif ox_coord_text in value or loc_table_head_four_text in value:
                self.__ox_coord.configure(text=new_text)
                self.__locations_table[0][3].configure(text=new_text)
            elif oy_coord_text in value or loc_table_head_five_text in value:
                self.__oy_coord.configure(text=new_text)
                self.__locations_table[0][4].configure(text=new_text)
            elif location_name_text in value:
                self.__location_name.configure(text=new_text)
            elif emp_table_head_one_text in value:
                self.__employees_table[0][0].configure(text=new_text)
            elif emp_table_head_two_text in value:
                self.__employees_table[0][1].configure(text=new_text)
            elif emp_table_head_three_text in value:
                self.__employees_table[0][2].configure(text=new_text)
            elif emp_table_head_four_text in value:
                self.__employees_table[0][3].configure(text=new_text)
            elif loc_table_head_one_text in value:
                self.__locations_table[0][0].configure(text=new_text)
            elif loc_table_head_two_text in value:
                self.__locations_table[0][1].configure(text=new_text)
            elif loc_table_head_three_text in value:
                self.__locations_table[0][2].configure(text=new_text)

    def get_coordinator_window(self):
        return self.__coordinator_window

    def get_password_field(self):
        return self.__password_text_field

    def get_new_password_field(self):
        return self.__new_password_text_field

    def get_generate_route_button(self):
        return self.__route_button

    def get_change_password_button(self):
        return self.__password_button

    def get_acctual_name_label(self):
        return self.__acctual_name_label

    def get_csv_report_button(self):
        return self.__csv_button

    def get_json_report_button(self):
        return self.__json_button

    def get_xml_report_button(self):
        return self.__xml_button

    def get_employees_table(self):
        return self.__employees_table

    def get_locations_table(self):
        return self.__locations_table

    def get_update_employees_locations_button(self):
        return self.__update_employees_locations_button

    def get_add_new_location_button(self):
        return self.__add_new_location_button

    def get_update_locations_button(self):
        return self.__update_locations_button

    def get_delete_location_button(self):
        return self.__delete_location_button

    def get_new_location_name(self):
        return self.__new_location_name_field

    def get_ox_coord(self):
        return self.__ox_coord_field

    def get_oy_coord(self):
        return self.__oy_coord_field

    def get_location_name(self):
        return self.__location_name_field

    def get_tabs(self):
        return self.__pages

    def get_french_language_button(self):
        return self.__french_language_button

    def get_english_language_button(self):
        return self.__english_language_button

    def get_romanian_language_button(self):
        return self.__romanian_language_button

    def get_spanish_language_button(self):
        return self.__spanish_language_button

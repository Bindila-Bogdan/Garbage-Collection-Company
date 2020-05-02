from tkinter import *
from tkinter import messagebox


class LoginView:
    def __init__(self, base_view):
        self.__login_window = base_view

        self.__login_frame = Frame(self.__login_window, bg="#64b167")
        self.__logo_img = PhotoImage(file="../images/logo.png")
        self.__logo_label = Label(self.__login_frame)
        self.__logo_label.config(image=self.__logo_img)
        self.__logo_label.pack(pady=(110, 0))
        self.__username_label = Label(self.__login_frame, text="Username", bg="#64b167", anchor=W)
        self.__username_label.config(font=("fixedsys", "24"))
        self.__username_label.pack(padx=(12, 88), pady=(32, 0))
        self.__username_text_field = Entry(self.__login_frame, width=15)
        self.__username_text_field.config(font=("fixedsys", "18"))
        self.__username_text_field.pack(padx=15, pady=(0, 15))
        self.__password_label = Label(self.__login_frame, text="Password", bg="#64b167")
        self.__password_label.config(font=("fixedsys", "24"))
        self.__password_label.pack(padx=(15, 91), pady=(15, 0))
        self.__password_text_field = Entry(self.__login_frame, width=15)
        self.__password_text_field.config(font=("fixedsys", "18"))
        self.__password_text_field.pack(padx=15, pady=(0, 64))
        self.__login_img = PhotoImage(file="../images/login.png")
        self.__login_button = Button(self.__login_frame, width=128, height=64, relief=RIDGE,
                                     bd=2, cursor="hand2", image=self.__login_img, bg="#64b167")
        self.__login_button.pack(padx=(5, 5), pady=(5, 84))
        self.__login_frame.pack(fill="y", pady=(60, 0))

    @staticmethod
    def show_warning():
        messagebox.showwarning("Wrong credentials", "Incorrect username or password.")

    def get_login_window(self):
        return self.__login_window

    def get_username_text_field(self):
        return self.__username_text_field

    def get_password_text_field(self):
        return self.__password_text_field

    def get_login_button(self):
        return self.__login_button

    def clean(self):
        for widget in self.__login_window.winfo_children():
            widget.destroy()

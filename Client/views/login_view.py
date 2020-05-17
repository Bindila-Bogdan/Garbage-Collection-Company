from tkinter import *
from tkinter import messagebox
from language_manager.language_observer import LanguageObserver


class LoginView(LanguageObserver):
    def __init__(self, base_view):
        self.__login_window = base_view

        self.__login_frame = Frame(self.__login_window, bg="#64b167")
        self.__logo_img = PhotoImage(file="../images/logo.png")
        self.__logo_label = Label(self.__login_frame)
        self.__logo_label.config(image=self.__logo_img)
        self.__logo_label.pack(pady=(110, 0))
        self.__username_label = Label(self.__login_frame, text="Username", bg="#64b167", anchor=W)
        self.__username_label.config(font=("fixedsys", "24"))
        self.__username_label.pack(padx=(0, 0), pady=(32, 0))
        self.__username_text_field = Entry(self.__login_frame, width=15)
        self.__username_text_field.config(font=("fixedsys", "18"))
        self.__username_text_field.pack(padx=15, pady=(0, 15))
        self.__password_label = Label(self.__login_frame, text="Password", bg="#64b167")
        self.__password_label.config(font=("fixedsys", "24"))
        self.__password_label.pack(padx=(0, 0), pady=(15, 0))
        self.__password_text_field = Entry(self.__login_frame, width=15)
        self.__password_text_field.config(font=("fixedsys", "18"))
        self.__password_text_field.pack(padx=15, pady=(0, 64))
        self.__login_img = PhotoImage(file="../images/login.png")
        self.__login_button = Button(self.__login_frame, width=128, height=64, relief=RIDGE,
                                     bd=2, cursor="hand2", image=self.__login_img, bg="#ffffff")
        self.__login_button.pack(padx=(5, 5), pady=(5, 32))
        self.__login_frame.pack(fill="y", pady=(60, 0))

        self.__language_frame = Frame(self.__login_window, bg="#64b167")
        self.__french_img = PhotoImage(file="../images/french.png")
        self.__french_language_button = Button(self.__language_frame, width=66, height=44, relief=RIDGE,
                                               bd=2, cursor="hand2", image=self.__french_img, bg="#ffffff")
        self.__french_language_button.grid(row=0, column=0, sticky="w", pady=(5, 32), padx=(53, 8))

        self.__english_img = PhotoImage(file="../images/english.png")
        self.__english_language_button = Button(self.__language_frame, width=66, height=44, relief=RIDGE,
                                                bd=2, cursor="hand2", image=self.__english_img, bg="#ffffff")
        self.__english_language_button.grid(row=0, column=1, sticky="w", pady=(5, 32), padx=(16, 8))

        self.__romanian_img = PhotoImage(file="../images/romanian.png")
        self.__romanian_language_button = Button(self.__language_frame, width=66, height=44, relief=RIDGE,
                                                 bd=2, cursor="hand2", image=self.__romanian_img, bg="#ffffff")
        self.__romanian_language_button.grid(row=0, column=2, sticky="w", pady=(5, 32), padx=(16, 8))

        self.__spanish_img = PhotoImage(file="../images/spanish.png")
        self.__spanish_language_button = Button(self.__language_frame, width=66, height=44, relief=RIDGE,
                                                bd=2, cursor="hand2", image=self.__spanish_img, bg="#ffffff")
        self.__spanish_language_button.grid(row=0, column=3, sticky="w", pady=(5, 32), padx=(16, 62))
        self.__language_frame.pack(fill="y", pady=(0, 0))

    @staticmethod
    def show_warning():
        messagebox.showwarning("Wrong credentials", "Incorrect username or password.")

    def clean(self):
        for widget in self.__login_window.winfo_children():
            widget.destroy()

    def update(self, dictionary, index):
        username_label_text = self.__username_label['text']
        password_label_text = self.__password_label['text']
        for (_, value) in dictionary.items():
            new_text = value[index]
            if username_label_text in value:
                self.__username_label.configure(text=new_text)
            elif password_label_text in value:
                self.__password_label.configure(text=new_text)

    def get_login_window(self):
        return self.__login_window

    def get_username_text_field(self):
        return self.__username_text_field

    def get_password_text_field(self):
        return self.__password_text_field

    def get_login_button(self):
        return self.__login_button

    def get_french_language_button(self):
        return self.__french_language_button

    def get_english_language_button(self):
        return self.__english_language_button

    def get_romanian_language_button(self):
        return self.__romanian_language_button

    def get_spanish_language_button(self):
        return self.__spanish_language_button

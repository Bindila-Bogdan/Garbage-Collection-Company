from tkinter import *


class BaseView:
    def __init__(self):
        self.__base_window = Tk()
        self.__base_window.title("GCC")
        self.__base_window.bind("<Escape>", lambda e: self.__base_window.destroy())
        self.__base_window.attributes("-fullscreen", True)

    def get_window(self):
        return self.__base_window

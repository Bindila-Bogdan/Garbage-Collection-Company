from language_manager.language_subject import LanguageSubject


class ConcreteLanguageSubject(LanguageSubject):
    def __init__(self, language_dictionary):
        self.__observers = []
        self.__language = "romanian"
        self.__language_dictionary = language_dictionary

    def notify(self):
        if self.__language == "french":
            dictionar_index = 0
        elif self.__language == "english":
            dictionar_index = 1
        elif self.__language == "romanian":
            dictionar_index = 2
        else:
            dictionar_index = 3
        for observer in self.__observers:
            observer.update(self.__language_dictionary, dictionar_index)

    def attach(self, observer):
        print("Observer added.")
        if observer is not self.__observers:
            self.__observers.append(observer)

    def detach(self, observer):
        if observer in self.__observers:
            self.__observers.remove(observer)
            print("Observer detached.")

    def set_language(self, language):
        if language == "french" or language == "english" or language == "romanian" or language == "spanish":
            self.__language = language
            print("Language set to: {}.".format(language))

    def get_language(self):
        return self.__language

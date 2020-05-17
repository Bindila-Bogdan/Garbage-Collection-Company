import pickle


class LanguagePersistence:
    def __init__(self):
        self.__language_data = {}
        self.__file_name = "language_data"

    def populate_language_dictionary(self):
        self.__language_data[0] = ["Nom complet", "Full name", "Nume intreg", "Nombre completo"]
        self.__language_data[1] = ["Nom d'utilisateur", "Username", "Nume utilizator", "Nombre de usuario"]
        self.__language_data[2] = ["Mot de passe", "Password", "Parola", "Contraseña"]
        self.__language_data[3] = ["Ancien mot de passe", "Old password", "Parola veche", "Contraseña anterior"]
        self.__language_data[4] = ["Nouveau mot de passe", "New password", "Parola noua", "Nueva contraseña"]
        self.__language_data[5] = ["Changer le mot de passe", "Change password", "Schimba parola",
                                   "Cambia la contraseña"]
        self.__language_data[6] = ["Emplacement", "Location", "Locatie", "Localización"]
        self.__language_data[7] = ["Coordinador", "Coordinator", "Coordonator", "Coordinador"]
        self.__language_data[8] = [" Coordinators ", " Coordinators ", " Coordonatori ", " Coordinadores "]
        self.__language_data[9] = ["Générer un itinéraire", "Generate route", "Genereaza ruta", "Generar ruta"]
        self.__language_data[10] = ["Rapport CSV", "CSV Report", "Raport CSV", "Informe CSV"]
        self.__language_data[11] = ["Rapport JSON", "JSON Report", "Raport JSON", "Informe JSON"]
        self.__language_data[12] = ["Rapport XML", "XML Report", "Raport XML", "Informe XML"]
        self.__language_data[13] = [" Carte ", " Map ", " Harta ", " Mapa "]
        self.__language_data[14] = [" Emplacements ", " Locations ", " Locatii ", " Localizaciones "]
        self.__language_data[15] = ["Prénom", "First name", "Prenume", "Nombre de pila"]
        self.__language_data[16] = ["Nom de famille", "Last name", "Nume de familie", "Apellido"]
        self.__language_data[17] = ["Mettre à jour les emplacements attribués", "Update locations assigned",
                                    "Actualizeaza locatiile atribuite", "Actualizar ubicaciones asignadas"]
        self.__language_data[18] = ["Nombre", "Number", "Numar", "Nombre"]
        self.__language_data[19] = ["Employé", "Employee", "Angajat", "Empleado"]
        self.__language_data[20] = [" Employés ", " Employees ", " Angajati ", " Empleados "]
        self.__language_data[21] = ["Location name", "Location name", "Numele locatiei", "Nombre del lugar"]
        self.__language_data[22] = ["Ox coordinate", "Ox coordinate", "Coordonata Ox", "Ox coordinar"]
        self.__language_data[23] = ["Oy coordinate", "Oy coordinate", "Coordonata Oy", "Oy coordinar"]
        self.__language_data[24] = ["No", "No", "No", "No"]
        self.__language_data[25] = [" Employés coordonnés ", " Coordinated Employees ", " Angajati coordonati ",
                                    " Empleados coordinados "]
        self.__language_data[26] = ["Add new location", "Add new location", "Adauga o locatie noua",
                                    "Agregar una nueva ubicación"]
        self.__language_data[27] = ["Mettre à jour les emplacements", "Update locations", "Actualizeaza locatiile",
                                    "Actualizar ubicaciones"]
        self.__language_data[28] = ["Supprimer le lieu", "Delete location", "Sterge locatia", "Eliminar ubicación"]
        self.__language_data[29] = ["Nouveau nom d'emplacement", "New location name", "Nume nou de locatie",
                                    "Nuevo nombre de ubicación"]
        self.__language_data[30] = ["Entrez le nom du lieu", "Enter location name", "Introdu numele locatiei",
                                    "Ingrese el nombre de la ubicación"]
        self.__language_data[31] = ["Ajouter un nouveau coordinateur", "Add new coordinator",
                                    "Adauga un nou coordonator", "Agregar nuevo coordinador"]
        self.__language_data[32] = ["Coordonnateur de la mise à jour", "Update coordinator",
                                    "Actualizeaza coordonatorul", "Coordinador de actualizaciones"]
        self.__language_data[33] = ["Supprimer le coordinateur", "Delete coordinator", "Sterge coodonatorul",
                                    "Eliminar coordinador"]
        self.__language_data[34] = ["Ajouter un nouvel employé", "Add new employee", "Adauga un angajat",
                                    "Agregar nuevo empleado"]
        self.__language_data[35] = ["Mettre à jour l'employé", "Update employee", "Actualizeaza anagajatul",
                                    "Actualizar empleado"]
        self.__language_data[36] = ["Supprimer un employé", "Delete employee", "Sterge angajatul", "Eliminar empleado"]

    def write_language_data(self):
        self.populate_language_dictionary()
        print("Language data writing...")
        with open(self.__file_name + ".bin", "wb") as language_data_out:
            pickle.dump(self.__language_data, language_data_out)

    def read_language_data(self):
        print("Language data reading...")
        with open("../language_manager/" + self.__file_name + ".bin", "rb") as language_data_in:
            self.__language_data = pickle.load(language_data_in)

    def get_language_data(self):
        return self.__language_data

    def show_dictionary(self):
        for (key, value) in self.__language_data.items():
            print("{} : {}".format(key, value))

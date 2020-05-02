class Location:
    def __init__(self, name, coord_ox, coord_oy):
        self.__name = name
        self.__coord_ox = coord_ox
        self.__coord_oy = coord_oy

    def get_name(self):
        return self.__name

    def get_coord_ox(self):
        return self.__coord_ox

    def get_coord_oy(self):
        return self.__coord_oy

    def set_name(self, name):
        self.__name = name

    def set_coord_ox(self, coord_ox):
        self.__coord_ox = coord_ox

    def set_coord_oy(self, coord_oy):
        self.__coord_oy = coord_oy

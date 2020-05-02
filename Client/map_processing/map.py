import math
import numpy as np
from model.location import Location


class Map:
    def __init__(self, map_size, locations, number_of_generated_locations=0):
        self.__map_size = map_size
        self.__number_of_locations = len(locations)
        self.__number_of_generated_locations = number_of_generated_locations
        self.__locations = locations
        self.__generated_locations = []
        self.__map = None

    def get_location_names(self):
        location_names = []
        for location in self.__locations:
            location_names.append(location.get_name())
        return location_names

    def get_locations(self):
        return self.__locations

    def set_locations(self, locations):
        self.__locations = locations
        self.__number_of_locations = len(locations)

    def get_number_of_locations(self):
        return self.__number_of_locations

    def generate_locations(self):
        coords_ox = []
        coords_oy = []
        c_ox = np.random.uniform(0.0, self.__map_size, self.__number_of_generated_locations * 10)
        c_oy = np.random.uniform(0.0, self.__map_size, self.__number_of_generated_locations * 10)
        c_ox.sort()
        for index in range(self.__number_of_generated_locations):
            coords_ox.append(c_ox[index * 10])
            coords_oy.append(c_oy[index * 10])
        for index in range(self.__number_of_generated_locations):
            location = Location(index, round(coords_ox[index], 2), round(coords_oy[index], 2))
            self.__generated_locations.append(location)

    def get_generated_location_names(self):
        location_names = []
        for location in self.__generated_locations:
            location_names.append(location.get_name())
        return location_names

    def get_generated_locations(self):
        return self.__generated_locations

    def get_number_of_generated_locations(self):
        return self.__number_of_generated_locations

    def generate_map(self):
        self.__map = [[0 for _ in range(self.__number_of_locations)] for _ in range(self.__number_of_locations)]
        for row_index in range(self.__number_of_locations):
            for col_index in range(self.__number_of_locations):
                try:
                    if row_index != col_index and row_index:
                        first_location = self.__locations[row_index]
                        second_location = self.__locations[col_index]
                        distance2 = math.sqrt(
                            pow(float(first_location.get_coord_ox()) - float(second_location.get_coord_ox()), 2) +
                            pow(float(first_location.get_coord_oy()) - float(second_location.get_coord_oy()), 2))
                        self.__map[row_index][col_index] = self.__map[col_index][row_index] = round(distance2, 2)
                except TypeError:
                    pass

    def get_map(self):
        return self.__map

    def set_map_size(self, map_size):
        self.__map_size = map_size

    def get_map_size(self):
        return self.__map_size

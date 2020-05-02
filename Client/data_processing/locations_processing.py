from model.location import Location


class LocationsProcessing:
    def __init__(self, server_communication):
        self.__locations = []
        self.__map_size = 1000
        self.__server_communication = server_communication

    def set_locations(self, locations):
        self.__locations = locations

    def check_location(self, coord_ox, coord_oy):
        for location in self.__locations:
            if float(coord_ox) == float(location.get_coord_ox()) and float(coord_oy) == float(location.get_coord_oy()):
                return False
        return True

    def get_locations(self):
        return self.__locations

    def get_locations_names(self):
        location_names = []
        for location in self.__locations:
            location_names.append(str(location.get_name()))
        return location_names

    def modify_current_location(self, location_name, coord_ox, coord_oy):
        if float(coord_ox) > self.__map_size or float(coord_ox) < 0 or float(coord_oy) > self.__map_size or float(
                coord_oy) < 0:
            return
        if not self.check_location(float(coord_ox), float(coord_oy)):
            return
        data = [location_name, coord_ox, coord_oy]
        updated_data = self.__server_communication.communicate(1, data)
        self.__locations = updated_data[1]

    def add_current_location(self, location_name, coord_ox, coord_oy):
        if float(coord_ox) > self.__map_size or float(coord_ox) < 0 or float(coord_oy) > self.__map_size or float(
                coord_oy) < 0:
            return
        if not self.check_location(float(coord_ox), float(coord_oy)):
            return
        location_names = [location.get_name() for location in self.__locations]
        if location_name in location_names:
            return
        data = [location_name, coord_ox, coord_oy]
        updated_data = self.__server_communication.communicate(2, data)
        self.__locations = updated_data[1]

    def delete_current_location(self, name_of_location):
        data = [name_of_location, None]
        updated_data = self.__server_communication.communicate(3, data)
        self.__locations = updated_data[1]

    def display_locations(self):
        print("*Locations*")
        for location in self.__locations:
            print("Name: " + '%2s' % str(location.get_name()), end=" ")
            print("Ox:" + '%6s' % str(location.get_coord_ox()), end=" ")
            print("Oy:" + '%6s' % str(location.get_coord_oy()))

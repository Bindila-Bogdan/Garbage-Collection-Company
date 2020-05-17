from databse_access.database_manager import DatabaseManager
from databse_access.employee_persistence import EmployeePersistence
from mysql.connector.errors import IntegrityError
from databse_access.persistence import Persistence
from model.location import Location


class LocationPersistence(Persistence):
    def __init__(self):
        super().__init__("Location_Persistence")
        self.__locations = []

    @staticmethod
    def add_location(name, coord_ox, coord_oy):
        connection, cursor = DatabaseManager.connect()
        add_location_statement = "INSERT INTO location (name, coord_ox, coord_oy) VALUES (%s, %s, %s)"
        values = (name, coord_ox, coord_oy)
        try:
            cursor.execute(add_location_statement, values)
            connection.commit()
        except IntegrityError:
            pass
        connection.close()

    @staticmethod
    def delete_location(name):
        name = str(name)
        EmployeePersistence.remove_locations_from_employees(name)

        connection, cursor = DatabaseManager.connect()
        delete_location_statement = "DELETE FROM location where name = " + name
        cursor.execute(delete_location_statement)
        connection.commit()
        connection.close()

    @staticmethod
    def update_location(name, coord_ox, coord_oy):
        connection, cursor = DatabaseManager.connect()
        update_location_statement = "UPDATE location SET coord_ox = %s, coord_oy = %s WHERE name = %s"
        values = (coord_ox, coord_oy, name)
        try:
            cursor.execute(update_location_statement, values)
            connection.commit()
        except IntegrityError:
            pass
        connection.close()

    @staticmethod
    def display_locations():
        connection, cursor = DatabaseManager.connect()
        get_location_statement = "SELECT * FROM location"
        cursor.execute(get_location_statement)
        locations = cursor.fetchall()
        connection.close()
        for location in locations:
            print(location)

    def get_data(self):
        connection, cursor = DatabaseManager.connect()
        get_location_statement = "SELECT * FROM location"
        cursor.execute(get_location_statement)
        locations = cursor.fetchall()
        connection.close()
        self.__locations = []
        for location in locations:
            self.__locations.append(Location(location[0], location[1], location[2]))
        return self.__locations

    @staticmethod
    def get_location_with_name(name):
        connection, cursor = DatabaseManager.connect()
        get_location_statement = "SELECT * FROM location WHERE name = " + name
        cursor.execute(get_location_statement)
        locations = cursor.fetchall()
        connection.close()
        return Location(locations[0][0], locations[0][1], locations[0][2])

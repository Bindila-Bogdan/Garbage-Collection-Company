import mysql.connector


class DatabaseManager:
    @staticmethod
    def connect_without_table():
        initial_connection = mysql.connector.connect(
            host="localhost",
            username="root",
            password="root"
        )
        initial_cursor = initial_connection.cursor()
        return initial_connection, initial_cursor

    @staticmethod
    def connect():
        connection = mysql.connector.connect(
            host="localhost",
            username="root",
            password="root",
            database="gcc_db"
        )
        cursor = connection.cursor()
        return connection, cursor

    @staticmethod
    def create_database():
        connection, cursor = DatabaseManager.connect_without_table()
        cursor.execute("CREATE DATABASE gcc_db")
        connection.close()

    @staticmethod
    def create_tables():
        connection, cursor = DatabaseManager.connect()
        cursor.execute("""CREATE TABLE IF NOT EXISTS location (
                              name INT PRIMARY KEY,
                              coord_ox FLOAT NOT NULL,
                              coord_oy FLOAT NOT NULL,
                              CONSTRAINT location_constraint UNIQUE (coord_ox, coord_oy))""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS account (
                              id INT AUTO_INCREMENT PRIMARY KEY,
                              username VARCHAR(255) NOT NULL,
                              password VARCHAR(255) NOT NULL,
                              CONSTRAINT account_constraint UNIQUE (username, password))""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS administrator (
                              first_name VARCHAR(255),
                              last_name VARCHAR(255),
                              PRIMARY KEY (first_name, last_name),
                              account_id INT UNIQUE NOT NULL,
                              FOREIGN KEY (account_id) REFERENCES account(id))""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS coordinator (
                              first_name VARCHAR(255),
                              last_name VARCHAR(255),
                              PRIMARY KEY (first_name, last_name),
                              account_id INT UNIQUE NOT NULL,
                              FOREIGN KEY (account_id) REFERENCES account(id))""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS employee (
                              first_name VARCHAR(255),
                              last_name VARCHAR(255),
                              PRIMARY KEY(first_name, last_name),
                              coordinator_first_name VARCHAR(255),
                              coordinator_last_name VARCHAR(255),
                              FOREIGN KEY (coordinator_first_name, coordinator_last_name)
                              REFERENCES coordinator(first_name, last_name),
                              loc_id INT UNIQUE,
                              FOREIGN KEY (loc_id) REFERENCES location(name),
                              account_id INT UNIQUE NOT NULL,
                              FOREIGN KEY (account_id) REFERENCES account(id))""")
        connection.close()

    @staticmethod
    def delete_tables():
        connection, cursor = DatabaseManager.connect()
        cursor.execute("DROP TABLE IF EXISTS employee")
        cursor.execute("DROP TABLE IF EXISTS coordinator")
        cursor.execute("DROP TABLE IF EXISTS administrator")
        cursor.execute("DROP TABLE IF EXISTS location")
        cursor.execute("DROP TABLE IF EXISTS account")
        connection.close()

    @staticmethod
    def truncate_tables():
        connection, cursor = DatabaseManager.connect()
        cursor.execute("TRUNCATE TABLE IF EXISTS employee")
        cursor.execute("TRUNCATE TABLE IF EXISTS coordinator")
        cursor.execute("TRUNCATE TABLE IF EXISTS administrator")
        cursor.execute("TRUNCATE TABLE IF EXISTS location")
        cursor.execute("TRUNCATE TABLE IF EXISTS account")
        connection.close()

    @staticmethod
    def repopulate_tables(location_persistance, employee_persistance):
        loc_1 = ("1", "10.42", "598.45")
        loc_2 = ("8", "103.39", "851.78")
        loc_3 = ("23", "218.29", "29.16")
        loc_4 = ("42", "354.93", "581.4")
        loc_5 = ("89", "838.42", "718.74")
        locations = [loc_1, loc_2, loc_3, loc_4, loc_5]

        for location in locations:
            location_persistance.add_location(location[0], location[1], location[2])

        employee_1 = ("Dominic", "Vega", True)
        employees = [employee_1]

        coordinator_1 = ("Conan", "Myles", False)
        coordinator_2 = ("Zac", "Morse", False)
        coordinators = [coordinator_1, coordinator_2]

        administrator = ("Bindila", "Bogdan", None)

        for employee in employees:
            employee_persistance.add_employee(employee[0], employee[1], employee[2])

        for coordinator in coordinators:
            employee_persistance.add_employee(coordinator[0], coordinator[1], coordinator[2])

        employee_persistance.add_employee(administrator[0], administrator[1], administrator[2])

        employee_persistance.set_location(employees[0][0], employees[0][1], locations[1][0])
        employee_persistance.set_coordinator(employees[0][0], employees[0][1], coordinators[0][0], coordinators[0][1])

    @staticmethod
    def recreate_database(location_persistance, employee_persistance):
        DatabaseManager.delete_tables()
        DatabaseManager.create_tables()
        DatabaseManager.repopulate_tables(location_persistance, employee_persistance)

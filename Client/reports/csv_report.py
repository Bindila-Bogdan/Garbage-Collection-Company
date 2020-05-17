import csv


class CSVReport:
    def __init__(self):
        self.__csv_data = None

    def write_in_csv_file(self, coordinator_name):
        print("*CSV*")
        with open("../reports/locations_persistence_" + coordinator_name + ".csv", 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(self.__csv_data)

    def read_from_csv_file(self, coordinator_name):
        with open("../reports/locations_persistence_" + coordinator_name + ".csv", "r") as csv_file:
            self.__csv_data = csv.reader(csv_file)
            print("*CSV*")
            for data in self.__csv_data:
                print(data)

    def set_csv_data(self, csv_data):
        self.__csv_data = csv_data

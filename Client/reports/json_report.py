import json


class JSONReport:
    def __init__(self):
        self.__json_data = None

    def write_in_json_file(self, coordinator_name):
        print("*JSON*")
        with open("../reports/locations_persistence_" + coordinator_name + ".json", "w") as json_file:
            json.dump(self.__json_data, json_file, indent=4)

    def read_from_json_file(self, coordinator_name):
        with open("../reports/locations_persistence_" + coordinator_name + ".json") as json_file:
            self.__json_data = json.load(json_file)
            print("*JSON*")
            for data in self.__json_data:
                print(data)

    def set_json_data(self, json_data):
        self.__json_data = json_data

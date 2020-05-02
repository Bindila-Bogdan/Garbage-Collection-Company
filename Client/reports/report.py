from model.employee import Employee
import xml.etree.ElementTree as Et
from xml.dom import minidom
import copy
import json
import csv


class Report:
    def __init__(self):
        self.__csv_data = None
        self.__json_data = None
        self.__xml_data = None

    def generate_locations_data(self, locations, employees):
        self.__csv_data = [[] for _ in range(len(locations) + 1)]
        self.__json_data = [{} for _ in range(len(locations))]
        self.__csv_data[0] = ["Employee", "Location_Name", "Ox", "Oy"]
        index = 0
        for location in locations:
            index += 1
            assigned = False
            for employee in employees:
                if isinstance(employee, Employee):
                    if location.get_name() == employee.get_location():
                        assigned = True
                        self.__json_data[index - 1][
                            "Employee"] = employee.get_first_name() + "_" + employee.get_last_name()
                        self.__csv_data[index].append(employee.get_first_name() + "_" + employee.get_last_name())
            if not assigned:
                self.__csv_data[index].append("Not assigned")
                self.__json_data[index - 1]["Employee"] = "Not assigned"
            self.__csv_data[index].append(location.get_name())
            self.__csv_data[index].append(location.get_coord_ox())
            self.__csv_data[index].append(location.get_coord_oy())
            self.__json_data[index - 1]["Location_Name"] = location.get_name()
            self.__json_data[index - 1]["Ox"] = location.get_coord_ox()
            self.__json_data[index - 1]["Oy"] = location.get_coord_oy()
            self.__xml_data = copy.deepcopy(self.__csv_data)

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

    def write_in_xml_file(self, coordinator_name):
        print("*XML*")
        locations_root = Et.Element("locations")
        if self.__xml_data is not None and len(self.__xml_data) >= 1:
            for i in range(1, len(self.__xml_data)):
                employee_name, location_name, ox_coord, oy_coord = self.__xml_data[i]
                location = Et.SubElement(locations_root, "location")
                Et.SubElement(location, "employee").text = employee_name
                Et.SubElement(location, "location_name").text = str(location_name)
                Et.SubElement(location, "ox_coordinate").text = str(ox_coord)
                Et.SubElement(location, "oy_coordinate").text = str(oy_coord)
        xml_as_string = Et.tostring(locations_root, 'utf-8')
        reparsed_xml = minidom.parseString(xml_as_string)
        refactored_xml = reparsed_xml.toprettyxml(indent="\t")
        with open("../reports/locations_persistence_" + coordinator_name + ".xml", "w") as locations_file:
            locations_file.write(refactored_xml)

    def read_from_xml_file(self, coordinator_name):
        self.__xml_data = []
        index = 0
        locations_root = Et.parse("../reports/locations_persistence_" + coordinator_name + ".xml").getroot()
        for location_tag in locations_root.findall("./location"):
            self.__xml_data.append([])
            for individual_tag in location_tag.findall("./"):
                self.__xml_data[index].append(individual_tag.text)
            index += 1
        print("*XML*")
        for data in self.__xml_data:
            print(data)

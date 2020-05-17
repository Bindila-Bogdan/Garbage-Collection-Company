import xml.etree.ElementTree as Et
from xml.dom import minidom


class XMLReport:
    def __init__(self):
        self.__xml_data = None

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

    def set_xml_data(self, xml_data):
        self.__xml_data = xml_data

from model.employee import Employee
from reports.csv_report import CSVReport
from reports.json_report import JSONReport
from reports.xml_report import XMLReport
import copy


class ReportBuilder:
    def __init__(self):
        self.__csv_report = CSVReport()
        self.__json_report = JSONReport()
        self.__xml_report = XMLReport()

    def generate_locations_data(self, locations, employees):
        csv_data = [[] for _ in range(len(locations) + 1)]
        json_data = [{} for _ in range(len(locations))]
        csv_data[0] = ["Employee", "Location_Name", "Ox", "Oy"]
        index = 0
        for location in locations:
            index += 1
            assigned = False
            for employee in employees:
                if isinstance(employee, Employee):
                    if location.get_name() == employee.get_location():
                        assigned = True
                        json_data[index - 1][
                            "Employee"] = employee.get_first_name() + "_" + employee.get_last_name()
                        csv_data[index].append(employee.get_first_name() + "_" + employee.get_last_name())
            if not assigned:
                csv_data[index].append("Not assigned")
                json_data[index - 1]["Employee"] = "Not assigned"
            csv_data[index].append(location.get_name())
            csv_data[index].append(location.get_coord_ox())
            csv_data[index].append(location.get_coord_oy())
            json_data[index - 1]["Location_Name"] = location.get_name()
            json_data[index - 1]["Ox"] = location.get_coord_ox()
            json_data[index - 1]["Oy"] = location.get_coord_oy()
            xml_data = copy.deepcopy(csv_data)
            self.__csv_report.set_csv_data(csv_data)
            self.__json_report.set_json_data(json_data)
            self.__xml_report.set_xml_data(xml_data)

    def get_csv_report(self):
        return self.__csv_report

    def get_json_report(self):
        return self.__json_report

    def get_xml_report(self):
        return self.__xml_report

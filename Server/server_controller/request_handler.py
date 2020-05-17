class RequestHandler:
    @staticmethod
    def handle_request(code, data, employee_persistance, location_persistance):
        if code == 0:
            employee_persistance.set_new_password(data[0], data[1], data[2], data[3])
        elif code == 1:
            location_persistance.update_location(data[0], data[1], data[2])
        elif code == 2:
            location_persistance.add_location(data[0], data[1], data[2])
        elif code == 3:
            location_persistance.delete_location(data[0])
        elif code == 4:
            employee_persistance.set_location(data[0], data[1], data[2])
        elif code == 5:
            employee_persistance.add_employee(data[0], data[1], data[2])
        elif code == 6:
            employee_persistance.set_coordinator(data[0], data[1], data[2], data[3])
        elif code == 7:
            employee_persistance.delete_employee(data[0], data[1], data[2])
        elif code == 8:
            employee_persistance.update_employee(data[0], data[1], data[2], data[3], data[4])

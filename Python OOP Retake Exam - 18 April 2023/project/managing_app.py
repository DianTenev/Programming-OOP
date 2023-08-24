from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        current_user = User(first_name, last_name, driving_license_number)
        try:
            tmp = [x for x in self.users if x.driving_license_number == current_user.driving_license_number][0]
            return f"{tmp.driving_license_number} has already been registered to our platform."
        except IndexError:
            self.users.append(current_user)
            return f"{current_user.first_name} {current_user.last_name} was successfully registered under " \
                   f"DLN-{current_user.driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ["PassengerCar", "CargoVan"]:
            return f"Vehicle type {vehicle_type} is inaccessible."
        try:
            tmp = [x for x in self.vehicles if x.license_plate_number == license_plate_number][0]
            if tmp:
                return f"{license_plate_number} belongs to another vehicle."
        except IndexError:
            self.vehicles.append(ManagingApp.VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number))
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point, end_point, length):
        current_route = Route(start_point, end_point, length, len(self.routes) + 1)
        try:
            tmp = [x for x in self.routes if
                   x.start_point == start_point and x.end_point == end_point and x.length == length][0]
            if tmp:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
        except IndexError:
            pass

        try:
            tmp = [x for x in self.routes if
                   x.start_point == start_point and x.end_point == end_point and x.length < length][0]
            if tmp:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
        except IndexError:
            pass

        try:
            tmp = [x for x in self.routes if
                   x.start_point == start_point and x.end_point == end_point and x.length > length][0]
            tmp.is_locked = True
            raise IndexError
        except IndexError:
            self.routes.append(current_route)
            return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        current_user = [x for x in self.users if driving_license_number == x.driving_license_number][0]
        current_vehicle = [x for x in self.vehicles if x.license_plate_number == license_plate_number][0]
        current_route = [x for x in self.routes if x.route_id == route_id][0]
        if current_user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if current_vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if current_route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        current_vehicle.drive(current_route.length)
        if is_accident_happened:
            current_vehicle.is_damaged = True
            current_user.decrease_rating()
        else:
            current_user.increase_rating()

        if current_vehicle.is_damaged:
            status = "Damaged"
        else:
            status = "OK"
        return f"{current_vehicle.brand} {current_vehicle.model} " \
               f"License plate: {current_vehicle.license_plate_number} " \
               f"Battery: {current_vehicle.battery_level}% " \
               f"Status: {status}"

    def repair_vehicles(self, count):
        damaged_vehicles = sorted([x for x in self.vehicles if x.is_damaged], key=lambda x: (x.brand, x.model))
        if count < len(damaged_vehicles):
            for i in range(count):
                damaged_vehicles[i].is_damaged = False
                damaged_vehicles[i].battery_level = 100
            return f"{count} vehicles were successfully repaired!"
        else:
            for i in damaged_vehicles:
                i.is_damaged = False
                i.battery_level = 100
            return f"{len(damaged_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        new_list = sorted(self.users, key=lambda x: x.rating, reverse=True)
        res = "*** E-Drive-Rent ***\n"
        res += "\n".join([str(x) for x in new_list])
        return res


app = ManagingApp()
print(app.register_user('Tisha', 'Reenie', '7246506'))
print(app.register_user('Bernard', 'Remy', 'CDYHVSR68661'))
print(app.register_user('Mack', 'Cindi', '7246506'))
print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))
print(app.upload_vehicle('PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))
print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))
print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))
print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))
print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))
print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))
print(app.allow_route('SOF', 'PLD', 144))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('SOF', 'PLD', 184))
print(app.allow_route('BUR', 'VAR', 86.999))
print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))
print(app.make_trip('7246506', 'CWP8032', 1, True))
print(app.make_trip('7246506', 'COUN199728', 1, False))
print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))
print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))
print(app.repair_vehicles(2))
print(app.repair_vehicles(20))
print(app.users_report())


import unittest

from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 150)

    def test_class_attributes(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_initialization(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(150, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_with_valid_values(self):
        self.vehicle.drive(50)
        self.assertEqual(37.5, self.vehicle.fuel)

    def test_drive_with_invalid_values(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_with_valid_values(self):
        self.vehicle.drive(60)
        self.vehicle.refuel(50)
        self.assertEqual(75, self.vehicle.fuel)

    def test_refuel_with_invalid_values(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_string_method(self):
        self.assertEqual("The vehicle has 150 horse"
                         " power with 100 fuel left and 1.25 fuel consumption", self.vehicle.__str__())


if __name__ == "__main__":
    unittest.main()

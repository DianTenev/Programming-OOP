class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


car = Car("a", "b", 1, 4)
car.make = " "
print(car)


import unittest


class CarManagerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("a", "b", 1, 4)

    def test_initialization_and_getters(self):
        self.assertEqual("a", self.car.make)
        self.assertEqual("b", self.car.model)
        self.assertEqual(1, self.car.fuel_consumption)
        self.assertEqual(4, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_with_valid_value(self):
        self.car.make = "c"
        self.assertEqual("c", self.car.make)

    def test_make_setter_with_invalid_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter_with_valid_value(self):
        self.car.model = "d"
        self.assertEqual('d', self.car.model)

    def test_model_setter_with_invalid_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_setter_with_valid_number(self):
        self.car.fuel_consumption = 2
        self.assertEqual(2, self.car.fuel_consumption)

    def test_fuel_consumption_setter_with_invalid_number(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_with_valid_value(self):
        self.car.fuel_capacity = 5
        self.assertEqual(5, self.car.fuel_capacity)

    def test_fuel_capacity_setter_with_invalid_number(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_setter_with_valid_value(self):
        self.car.fuel_amount = 5
        self.assertEqual(5, self.car.fuel_amount)

    def test_fuel_amount_setter_with_invalid_number(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_negative_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_valid_values(self):
        self.car.refuel(2)
        self.assertEqual(2, self.car.fuel_amount)

    def test_refuel_with_value_higher_than_capacity(self):
        self.car.refuel(5)
        self.assertEqual(4, self.car.fuel_amount)

    def test_drive_without_exception(self):
        self.car.fuel_amount = 4
        self.car.drive(40)
        self.assertEqual(3.6, self.car.fuel_amount)
        self.car.drive(360)
        self.assertEqual(0, self.car.fuel_amount)

    def test_drive_with_exception(self):
        self.car.fuel_amount = 2
        with self.assertRaises(Exception) as ex:
            self.car.drive(201)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    unittest.main()



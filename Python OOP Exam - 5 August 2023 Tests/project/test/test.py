from project.second_hand_car import SecondHandCar
import unittest


class SecondHandCarTests(unittest.TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("Test", "Type", 200, 5000)

    def test_initialization(self):
        self.assertEqual("Test", self.car.model)
        self.assertEqual("Type", self.car.car_type)
        self.assertEqual(200, self.car.mileage)
        self.assertEqual(5000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setter_with_valid_values(self):
        self.car.price = 2
        self.assertEqual(2, self.car.price)

    def test_price_setter_with_invalid_values(self):
        with self.assertRaises(ValueError) as ex:
            self.car.price = 1

        self.assertEqual('Price should be greater than 1.0!', str(ex.exception))

    def test_mileage_setter_with_valid_values(self):
        self.car.mileage = 200
        self.assertEqual(200, self.car.mileage)

    def test_mileage_setter_with_invalid_values(self):
        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 100

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ex.exception))

    def test_set_promotional_price_with_invalid_new_price(self):
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(6000)

        self.assertEqual('You are supposed to decrease the price!', str(ex.exception))

    def test_set_promo_price_with_valid_price(self):
        self.car.set_promotional_price(4000)
        self.assertEqual(4000, self.car.price)
        self.assertEqual('The promotional price has been successfully set.', self.car.set_promotional_price(3999))

    def test_need_repair_with_invalid_repair_price(self):
        self.assertEqual('Repair is impossible!', self.car.need_repair(3000, "Test"))

    def test_need_repair_with_valid_values(self):
        self.assertEqual(f'Price has been increased due to repair charges.', self.car.need_repair(2000, "Test"))
        self.assertEqual(7000, self.car.price)
        self.assertEqual(1, len(self.car.repairs))
        self.assertEqual("Test", self.car.repairs[0])

    def test_gt_method_with_error(self):
        other_car = SecondHandCar("Test", "Other", 1000, 2000)
        self.assertNotEqual(self.car.car_type, other_car.car_type)
        self.assertEqual('Cars cannot be compared. Type mismatch!', self.car > other_car)

    def test_gt_method_with_valid_values(self):
        other_car = SecondHandCar("Test", "Type", 1000, 2000)
        self.assertTrue(self.car > other_car)

    def test_str_method(self):
        self.assertEqual("""Model Test | Type Type | Milage 200km
Current price: 5000.00 | Number of Repairs: 0""", str(self.car))





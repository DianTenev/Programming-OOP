class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker("Test", 1000, 50)

    def test_initialization(self):
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(50, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_with_energy_higher_than_zero(self):
        self.worker.work()
        self.assertEqual(1000, self.worker.money)
        self.assertEqual(50 - 1, self.worker.energy)

        self.worker.work()
        self.assertEqual(1000 + 1000, self.worker.money)
        self.assertEqual(50 - 1 - 1, self.worker.energy)

    def test_work_with_energy_less_than_zero(self):
        worker = Worker("Test", 1000, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_rest(self):
        self.worker.rest()
        self.assertEqual(50 + 1, self.worker.energy)

    def test_get_info(self):
        self.assertEqual('Test has saved 0 money.', self.worker.get_info())


if __name__ == "__main__":
    unittest.main()

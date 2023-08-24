import unittest

from project.mammal import Mammal


class MammalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Test", "Dog", "MUUU")

    def test_initialization(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("Dog", self.mammal.type)
        self.assertEqual("MUUU", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound(self):
        self.assertEqual("Test makes MUUU", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("Test is of type Dog", self.mammal.info())


if __name__ == "__main__":
    unittest.main()
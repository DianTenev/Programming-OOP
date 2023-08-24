class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.lst = IntegerList(1, 2, 3)

    def test_initialization_with_integers(self):
        self.assertEqual(3, len(self.lst.get_data()))

    def test_initialization_with_one_float(self):
        lst = IntegerList(1, 2, 2.3)
        self.assertEqual(2, len(lst.get_data()))

    def test_get_data(self):
        result = self.lst.get_data()
        self.assertEqual(result, self.lst._IntegerList__data)

    def test_add_with_integer(self):
        self.lst.add(4)
        self.assertEqual(4, len(self.lst.get_data()))

    def test_add_with_non_integer(self):
        with self.assertRaises(ValueError) as ex:
            self.lst.add("asd")

        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual(3, len(self.lst.get_data()))

    def test_remove_index_in_range(self):
        current_index = 1
        self.assertEqual(2, self.lst.get_data()[current_index])
        self.lst.remove_index(1)
        self.assertEqual(2, len(self.lst.get_data()))

    def test_remove_index_out_of_range(self):
        self.assertEqual(3, len(self.lst.get_data()))

        with self.assertRaises(IndexError) as ex:
            self.lst.remove_index(4)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(3, len(self.lst.get_data()))

    def test_get_valid_index(self):
        self.assertEqual(3, len(self.lst.get_data()))
        element = self.lst.get(1)
        self.assertEqual(2, element)

    def test_get_invalid_index(self):
        self.assertEqual(3, len(self.lst.get_data()))

        with self.assertRaises(IndexError) as ex:
            self.lst.get(4)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(3, len(self.lst.get_data()))

    def test_valid_insert(self):
        self.assertEqual(3, len(self.lst.get_data()))
        self.lst.insert(2, 5)
        self.assertEqual([1, 2, 5, 3], self.lst.get_data())

    def test_invalid_index(self):
        self.assertEqual(3, len(self.lst.get_data()))

        with self.assertRaises(IndexError) as ex:
            self.lst.insert(4, 5)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(3, len(self.lst.get_data()))

    def test_invalid_type(self):
        self.assertEqual(3, len(self.lst.get_data()))

        with self.assertRaises(ValueError) as ex:
            self.lst.insert(2, "asd")

        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual(3, len(self.lst.get_data()))

    def test_get_biggest(self):
        self.assertEqual(3, len(self.lst.get_data()))
        self.assertEqual(3, self.lst.get_biggest())

    def test_get_index(self):
        index = self.lst.get_index(2)
        self.assertEqual(1, index)


if __name__ == "__main__":
    unittest.main()


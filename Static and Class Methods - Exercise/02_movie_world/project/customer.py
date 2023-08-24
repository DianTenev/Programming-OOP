from typing import List

from project.dvd import DVD


class Customer:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds: List[DVD] = []

    def __repr__(self):
        return f"{self.id}: {self.name}" \
               f" of age {self.age} has " \
               f"{len(self.rented_dvds)} rented DVD's ({', '.join([dvd.name for dvd in self.rented_dvds])})"


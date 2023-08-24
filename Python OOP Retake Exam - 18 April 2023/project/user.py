class User:
    def __init__(self, first_name, last_name, driving_license_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__driving_license_number = driving_license_number
        self.rating = 0
        self.is_blocked = False

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if not value.strip():
            raise ValueError("First name cannot be empty!")
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if not value.strip():
            raise ValueError("Last name cannot be empty!")
        self.__last_name = value

    @property
    def driving_license_number(self):
        return self.__driving_license_number

    @driving_license_number.setter
    def driving_license_number(self, value):
        if not value:
            raise ValueError("Driving license number is required!")
        self.__driving_license_number = value

    def increase_rating(self):
        if self.rating + 0.5 > 10:
            self.rating = 10
        else:
            self.rating += 0.5

    def decrease_rating(self):
        if self.rating - 2 < 0:
            self.rating = 0
            self.is_blocked = True
        else:
            self.rating -= 2

    def __str__(self):
        return f"{self.__first_name} {self.__last_name} " \
               f"Driving license: {self.__driving_license_number} " \
               f"Rating: {self.rating}"

# user = User("Dian", "Tenev", "A 7897 MT")
# print(user)
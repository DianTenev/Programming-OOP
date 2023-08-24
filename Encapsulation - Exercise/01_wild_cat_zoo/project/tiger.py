from project.animal import Animal


class Tiger(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender, 45)
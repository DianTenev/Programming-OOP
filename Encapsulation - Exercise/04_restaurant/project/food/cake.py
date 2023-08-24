from project.food.dessert import Dessert


class Cake(Dessert):
    PRICE = 5
    GRAMS = 250
    CALORIES = 1000

    def __init__(self, name):
        super().__init__(name, price=5, grams=250, calories=1000)
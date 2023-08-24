class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity):
        if self.quantity + quantity <= self.size:
            self.quantity += quantity

    def status(self):
        free_space = self.size - self.quantity
        return free_space


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
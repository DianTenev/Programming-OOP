class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current = 0
        self.last = -self.step

    def __iter__(self):
        return self

    def __next__(self):
        while self.current < self.count:
            self.last += self.step
            self.current += 1
            return self.last
        else:
            raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)

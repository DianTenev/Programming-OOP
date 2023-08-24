class countdown_iterator:
    def __init__(self, count):
        self.count = count + 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count < self.end:
            raise StopIteration
        return self.count


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")


class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number - 1
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current > self.number:
            raise StopIteration
        return self.sequence[self.current % len(self.sequence)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
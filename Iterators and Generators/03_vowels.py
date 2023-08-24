class vowels:
    def __init__(self, string: str):
        self.string = string
        self.list_vowels = ["a", "o", "u", "i", "e", "y"]
        self.start = -1
        self.end = len(self.string) - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start > self.end:
            raise StopIteration
        if self.string[self.start].lower() in self.list_vowels:
            return self.string[self.start]
        else:
            return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

class reverse_iter:
    def __init__(self, obj):
        self.obj = obj
        self.start = len(self.obj)
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start -= 1
        if self.start < self.end:
            raise StopIteration
        return self.obj[self.start]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

from typing import List


class BaseStack:
    def __init__(self):
        self.data: List[str] = []

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


class AddElement(BaseStack):
    def push(self, element):
        self.data.append(element)


class RemoveElement(BaseStack):
    def pop(self):
        return self.data.pop()


class TopElement(BaseStack):
    def top(self):
        return self.data[-1]


class Empty(BaseStack):
    def is_empty(self):
        if self.data:
            return False
        return True


class Stack(AddElement, RemoveElement, TopElement, Empty):
    pass


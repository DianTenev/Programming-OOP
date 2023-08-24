def reverse_text(string):
    start = len(string) - 1
    end = 0
    while start >= end:
        yield string[start]
        start -= 1


for char in reverse_text("step"):
    print(char, end='')

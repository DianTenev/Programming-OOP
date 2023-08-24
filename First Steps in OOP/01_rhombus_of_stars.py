def print_triangle(rows, count):
    print((rows - count) * " ", end="")
    print(*["*"] * count, sep=" ")


def first_triangle(rows):
    for count in range(1, rows + 1):
        print_triangle(rows, count)


def second_triangle(rows):
    for count in range(rows - 1, 0, -1):
        print_triangle(rows, count)


def print_rhombus():
    first_triangle(rows)
    second_triangle(rows)


rows = int(input())
print_rhombus()


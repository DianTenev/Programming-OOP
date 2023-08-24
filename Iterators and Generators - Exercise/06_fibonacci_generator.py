def fibonacci():
    previous_number = 0
    current_number = 1
    while True:
        if previous_number == 0:
            yield previous_number
        yield current_number
        tmp = current_number
        current_number += previous_number
        previous_number = tmp


generator = fibonacci()
for i in range(100):
    print(next(generator))

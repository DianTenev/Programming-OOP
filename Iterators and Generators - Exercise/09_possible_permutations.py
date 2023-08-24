from itertools import permutations


def possible_permutations(lst):
    perm = permutations(lst)
    for i in perm:
        yield list(i)


[print(n) for n in possible_permutations([1, 2, 3])]

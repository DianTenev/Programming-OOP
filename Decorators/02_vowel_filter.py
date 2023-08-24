def vowel_filter(function):
    def wrapper():
        return [i for i in function() if i in "ayuioe"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())

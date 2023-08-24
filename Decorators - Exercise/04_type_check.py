def type_check(current_type):
    def decorator(function):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, current_type):
                    return "Bad Type"

            return function(*args)
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))

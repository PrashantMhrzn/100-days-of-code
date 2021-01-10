# Skeleton Using Function

def decorator_func(func):
    def wrapper(*args, **kwargs):
        # some functionality
        return func(*args, **kwargs)
    return wrapper


# Skeleton Using Class

class decorator_class():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # some functonality
        return func(*args, **kwargs)


# Example

def timer(func):
    import datetime

    def wrapper(*args, **kwargs):
        t1 = datetime.datetime.now()
        results = func(*args, **kwargs)
        t2 = datetime.datetime.now()
        print(f'Ran {func.__name__} in {t2 - t1} seconds.')
        return results
    return wrapper


@timer
def func(name, age):
    print(f'func ran with arguments name: {name} and age: {age}')


func('tom', 40)

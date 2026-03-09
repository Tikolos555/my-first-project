def mack(return_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return return_value
        return wrapper
    return decorator

#@mock()
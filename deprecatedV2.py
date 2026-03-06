from warnings import warn
from functools import wraps


def deprecated(message):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            warn(message)
            return f(*args, **kwargs)
        return wrapper
    return decorator

@deprecated('пипец нафиг')
def f(x):
    return x

if __name__ == "__main__":
    print(f(1))
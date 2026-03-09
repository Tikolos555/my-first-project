def wraps(original):
    def decorator(wrapper):
        wrapper.__name__ = original.__name__
        wrapper.__doc__ = original.__doc__
        return wrapper
    return decorator



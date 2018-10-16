from flask_restly._storage import append_mapping
from functools import wraps


def patch(path, serializer=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)

            return ('', 204) if response is None else (response, 200)

        append_mapping(wrapper, path, serializer, 'PATCH')

        return wrapper

    return decorator

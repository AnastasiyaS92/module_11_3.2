import inspect
from pprint import pprint

info = {}


def introspection_info(obj):
    info['type'] = type(obj)
    info['attributes'] = [method for method in dir(obj) if not callable(getattr(obj, method))]
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    info['module'] = obj.__class__.__module__

    return info


number_info = introspection_info(42)
pprint(number_info)
print()

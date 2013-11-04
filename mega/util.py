__author__ = 'kimvais'


def check_if_str(obj):
    """
    Unified method of checking whether the object is a string on both
    Python 2 & 3
    """
    try:
        return isinstance(obj, basestring)
    except NameError:
        return isinstance(obj, str)


import calendar
from typing import NewType

Year = NewType('Year', int)

def custom_isleap(y: Year) -> bool:
    def print_isleap(y, result):
        print("{} {}".format(result, y))
    try:
        result = calendar.isleap(y)
    except TypeError:
        return False
    print_isleap(y, result)
    return result

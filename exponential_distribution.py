from math import log
from random import uniform


def exponential_number(number):
    return (-1 / number) * log(uniform(0, 1))

import numpy as np
import pytest


#
# print(0.1 + 0.1 + 0.1 == 0.3)
# print(0.3)
# print(0.1 + 0.1 + 0.1)

# assert 0.1 + 0.1 + 0.1 == 0.3, "Usual way to compare does not always work with floats!"


# example_argument = np.array([2081, 314942, 1059, 186606, 1148, 206186])
#
# print(example_argument.shape)
# print(example_argument)
#
# example_argument2 = np.array([2081, 314942, 1059, 186606, 1148, 206186], [])
#
# print(example_argument2.shape)
# print(example_argument2)
#

# example_argument = np.array([[
#     2081, 314942],
#     [
#         1059
#         ,
#         186606
#     ], [
#         1148
#         ,
#         206186
#     ], ])
# print(example_argument.shape)
# print(example_argument)


# <--- If context raised ValueError, silence it.
# <--- If the context did not raise ValueError, raise an exception.


def fun(actual):
    actual += actual + actual
    print(actual)
    return actual


fun(.1)

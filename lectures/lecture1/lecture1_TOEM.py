"""
Part 2, Lecture 1

Implement and test an argmax() function that returns the location of a maximum.

Tasks
-----

1.  Implement a function argmax() that takes a sequence of numbers and returns
    the index (position) of the maximum element.

2.  Test the function with the following sequence of numbers:
    [2, 3, -1, 7, 4]

3.  Add error handling if an empty sequence is passed. Test the function with an
    empty sequence.

4.  Use the notebook lecture1.ipynb to benchmark your implementation
    against NumPy's argmax().
"""

import numpy as np

values = [2, 3, -1, 7, 4]


def argmax(values):
    """
    return the index of the maximum value in a collect
    Parameters
    -------------
    values
        sequence of values

    Return
    ---------
    imax : int
        index of maximum
    """

    N = len(values)

    imax = None
    # set the vmax to lowest possible value
    vmax = -np.inf

    for i in range(N):
        # first iteration: value = 2
        value = values[i]
        if value > vmax:
            imax = i
            vmax = value

    return imax


imax = argmax(values)

print(f'The maximum is located at {imax}')

# Compare to NumPy's argmax
j = np.argmax(values)
print(f"The maximum is located at {j}")
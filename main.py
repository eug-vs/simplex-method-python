import simplex
from numpy import array, matrix


# Problem
c = array([2, 1, 0, 0, 0])

A = matrix([
    [-1, 1, 1, 0, 0],
    [1, -2, 0, 1, 0],
    [4, 1, 0, 0, 1],
])

b = array([3, 6, 22])

bounds = [
    (0, 5),
    (0, 4),
    (0, 8),
    (0, 14),
    (0, 22)
]

expected_result = [4.5, 4, 3.5, 9.5, 0]


# Initial plan and basis
x = [0, 0, 3, 6, 22]
basis = { 2, 3, 4 }


result = simplex.solve(c, A, b, bounds, x, basis)
assert all(result == expected_result), f"Result should be {expected_result}"


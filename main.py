import simplex
from numpy import inf


# Problem
c = [4, 1]

A = [
    [-4, 3],
    [2, 3],
]

b = [12, 30]

signs = [
    -1,
    -1
]

bounds = [
    (0, 6),
    (0, inf),
]

expected_result = [6, 6, 18, 0]

problem = simplex.to_standart_form(c, A, b, signs, bounds)
result = simplex.solve(*problem)

assert all(result == expected_result), f"Result should be {expected_result}"


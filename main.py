import numpy as np
from numpy import array, matrix, inf

a = 4
def test(a):
    a += 5

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

indices = set(range(5))


# Stage 1
# -//-


# Stage 2
x = [0, 0, 3, 6, 22]
basis = { 2, 3, 4 }

def stage2(c, A, b, bounds, indices, x, basis):
    print("Stage2")
    not_basis = []
    for j in indices:
        if j not in basis:
            not_basis.append(j)

    A_basis = np.delete(A, not_basis, axis=1)
    c_basis = np.delete(c, not_basis, axis=0)

    # A'u = c'
    u = np.linalg.solve(A_basis.transpose(), c_basis)
    print(u)

    # Estimates
    d = np.zeros(5)
    for j in not_basis:
        d[j] = c[j] - u * A[:, j]
    print(d)

    # Halting condition
    is_optimal = True
    for j in not_basis:
        if x[j] == bounds[j][0]: # Lower bound
            if d[j] > 0:
                is_optimal = False
                break
        if x[j] == bounds[j][1]: # Upper bound
            if d[j] < 0:
                is_optimal = False
                break
    else:
        print("Optimal solution!")
        return x

    print(is_optimal, j)

    # Choose j0
    j0 = j

    # Directions
    sign = np.sign(d[j0])

    l_basis_solution = np.linalg.solve(A_basis, - A[:, j0] * sign)
    l_basis= list(reversed(np.asarray(l_basis_solution.reshape(-1))[0]))

    l = np.zeros(5)
    for index in indices:
        if index == j0:
            l[index] = sign
        elif index in basis:
            l[index] = l_basis.pop()

    print(l)

    # Build steps
    steps = np.zeros(5)
    for j in indices:
        if j in basis:
            if l[j] > 0:
                steps[j] = (bounds[j][1] - x[j]) / l[j]
            elif l[j] < 0:
                steps[j] = (bounds[j][0] - x[j]) / l[j]
            else:
                steps[j] = inf
        elif j == j0:
            steps[j] = bounds[j][1] - bounds[j][0]
        else:
            steps[j] = inf

    max_step_index = np.argmin(steps)

    print(steps)
    print(max_step_index)

    # New basis
    if max_step_index in basis:
        basis.remove(max_step_index)
        basis.add(j0)

    print(basis)

    # New plan
    x += l * steps[max_step_index]
    print(x)
    return stage2(c, A, b, bounds, indices, x, basis)

result = stage2(c, A, b, bounds, indices, x, basis)
print(result)


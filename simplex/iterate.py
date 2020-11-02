import numpy as np


def iterate(c, A, b, bounds, x, basis):
    print("\nIteration:")
    print("basis:", basis)
    print("plan:", x)

    indices = range(len(c))

    # Build inverted basis
    size = len(c)
    not_basis = []
    for j in indices:
        if j not in basis:
            not_basis.append(j)

    # Vector of potentials
    A_basis = np.delete(A, not_basis, axis=1)
    c_basis = np.delete(c, not_basis, axis=0)
    u = np.linalg.solve(A_basis.transpose(), c_basis)
    print("u =", u)

    # Deltas
    deltas = np.zeros(size)
    for j in not_basis:
        deltas[j] = c[j] - u * A[:, j]
    print("deltas =", deltas)

    # Halting condition
    failing_indices = set()
    for j in not_basis:
        if x[j] == bounds[j][0]: # Lower bound
            if deltas[j] > 0:
                failing_indices.add(j)
        if x[j] == bounds[j][1]: # Upper bound
            if deltas[j] < 0:
                failing_indices.add(j)

    if not len(failing_indices):
        print("\nOptimal solution:", x)
        return x, basis

    # Choose j0
    j0 = np.argmax([abs(deltas[j]) if j in failing_indices else 0 for j in indices])
    print("Halting condition not met, keep going with j0 =", j0)

    # Directions
    sign = np.sign(deltas[j0])
    l_basis_solution = np.linalg.solve(A_basis, - A[:, j0] * sign)
    l_basis = list(reversed(np.asarray(l_basis_solution.reshape(-1))[0]))

    l = np.zeros(size)
    for index in indices:
        if index == j0:
            l[index] = sign
        elif index in basis:
            l[index] = l_basis.pop()
    print("l =", l)

    # Steps
    steps = np.zeros(size)
    for j in indices:
        if j in basis:
            if l[j] > 0:
                steps[j] = (bounds[j][1] - x[j]) / l[j]
            elif l[j] < 0:
                steps[j] = (bounds[j][0] - x[j]) / l[j]
            else:
                steps[j] = np.inf
        elif j == j0:
            steps[j] = bounds[j][1] - bounds[j][0]
        else:
            steps[j] = np.inf
    print("steps =", steps)

    # New basis
    max_step_index = np.argmin(steps)
    if max_step_index in basis:
        basis.remove(max_step_index)
        basis.add(j0)

    # New plan
    x += l * steps[max_step_index]

    return iterate(c, A, b, bounds, x, basis)


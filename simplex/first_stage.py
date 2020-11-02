import numpy as np
from numpy import append, eye
from simplex.iterate import iterate


def first_stage(c, A, b, bounds):
    """
    Compute initial basis and plan for the linear programming problem.

    Parameters:
        c: Vector which defines objective function
        A: Matrix - lefthand side of conditions system
        b: Vector - righthand side of conditions system
        bounds: Array of pairs (lower bound, upper bound) for each variable
    """

    size = len(c)
    equations_count = len(A)
    assert len(b) == equations_count, f"Righthand side should be provided for each equation"

    # Split indices randomly
    # TODO: allow choosing split beforehand
    split = range(int(size / 2))

    # Compute w
    x = [bounds[j][j in split] for j in range(size)]
    w = b - np.dot(A, x)
    w = list(np.asarray(w))[0]

    # Prepare initial basis and plan
    basis = set([i + size for i in range(equations_count)])
    x = [*x, *[abs(value) for value in w]]

    # Build first stage problem with artificial variables
    c = ([*[0] * size, *[-1] * equations_count])
    A = append(A, eye(equations_count), axis=1)

    # Match signs to w and setup bounds
    for i in range(equations_count):
        A[i, size + i] *= np.sign(w[i])
        bounds.append([0, abs(w[i])])

    return iterate(c, A, b, bounds, x, basis)


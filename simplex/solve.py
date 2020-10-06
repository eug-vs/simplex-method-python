from numpy import array, matrix, zeros
from simplex.iterate import iterate


def solve(c, A, b, bounds, basis):
    """
    Solve linear programming problem with a simplex method.

    Parameters:
        c: Vector which defines objective function
        A: Matrix - lefthand side of conditions system
        b: Vector - righthand side of conditions system
        bounds: Array of pairs (lower bound, upper bound) for each variable
        basis: Set of indices of artificial variables
    """

    c = array(c)
    A = matrix(A)
    size = len(c)
    assert A.shape[1] == size, f"Matrix A should have width {size}"
    assert len(bounds) == size, "Bounds should be provided for each variable"

    indices = range(size)

    # Build initial plan
    x = zeros(size)
    b_copy = list(b.copy())
    b_copy.reverse()
    for j in basis:
        x[j] = b_copy.pop()

    return iterate(c, A, b, bounds, indices, x, basis)


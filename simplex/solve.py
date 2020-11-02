from numpy import array, matrix, zeros
from simplex.iterate import iterate
from simplex.first_stage import first_stage


def solve(c, A, b, bounds):
    """
    Solve linear programming problem with a two-stage simplex method.

    Parameters:
        c: Vector which defines objective function
        A: Matrix - lefthand side of conditions system
        b: Vector - righthand side of conditions system
        bounds: Array of pairs (lower bound, upper bound) for each variable
    """

    c = array(c)
    A = matrix(A)
    size = len(c)
    assert A.shape[1] == size, f"Matrix A should have width {size}"
    assert len(bounds) == size, "Bounds should be provided for each variable"

    print("\n\nFIRST STAGE")
    x, basis = first_stage(c, A, b, bounds)

    print("\n\nSECOND STAGE")
    return iterate(c, A, b, bounds, x[:size], basis)[0]


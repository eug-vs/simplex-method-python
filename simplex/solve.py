import numpy as np
from simplex.stage2 import stage2


def solve(c, A, b, bounds, basis):
    size = len(c)
    assert A.shape[1] == size, f"Matrix A should have width {size}"
    assert len(bounds) == size, "Bounds should be provided for each variable"

    indices = range(size)

    # Build initial plan
    x = np.zeros(size)
    b_copy = list(b.copy())
    b_copy.reverse()
    for j in basis:
        x[j] = b_copy.pop()

    return stage2(c, A, b, bounds, indices, x, basis)


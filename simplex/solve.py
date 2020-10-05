from simplex.stage2 import stage2


def solve(c, A, b, bounds, x, basis):
    size = len(c)
    assert A.shape[1] == size, f"A should have width {size}"
    assert len(bounds) == size, f"Bounds should be provided for each variable"

    indices = range(size)
    return stage2(c, A, b, bounds, indices, x, basis)


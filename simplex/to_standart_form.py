from numpy import append, eye


def to_standart_form(c, A, b, bounds, signs):
    """
    Convert linear programming problem to the standart form.

    Parameters:
        c: Vector which defines objective function
        A: Matrix - lefthand side of conditions system
        b: Vector - righthand side of conditions system
        bounds: Array of pairs (lower bound, upper bound) for each variable
        signs: Array of signs of conditions system (1 for >, 0 for =, -1 for <)
    """

    variables_count = len(c)
    equations_count = len(A)
    assert len(b) == equations_count, f"Righthand side should be provided for each equation"
    assert len(signs) == equations_count, f"Sign should be provided for each equation"

    # Add artificial variables to basis
    basis = set(range(variables_count, variables_count + equations_count))
    print("Initial basis:", basis)

    # Append a bunch of zeroes to vector C for each artificial variable
    c = ([*c, *[0] * equations_count])

    # Compute bounds for artificial variables
    for lefthand, righthand, sign in zip(A, b, signs):
        new_bound = [0, 0]
        if sign:
            lefthand_extremum = sum(
                coeff * vbounds[sign * coeff > 0] for coeff, vbounds in zip(lefthand, bounds)
            )
            new_bound[1] = (lefthand_extremum - righthand) * sign
            new_bound.sort()
        bounds.append(new_bound)
    print("Bounds:", bounds)

    # Append identity matrix to A
    A = append(A, eye(equations_count), axis=1)

    return {
        "c": c,
        "A": A,
        "b": b,
        "bounds": bounds,
        "basis": basis,
    }


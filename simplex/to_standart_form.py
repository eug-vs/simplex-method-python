from numpy import array, matrix, append, inf, eye


def to_standart_form(c, A, b, signs, bounds):
    variables_count = len(c)
    equations_count = len(A)
    assert len(b) == equations_count, f"Righthand side should be provided for each equation"
    assert len(signs) == equations_count, f"Sign should be provided for each equation"

    # Add artificial variables to basis
    basis = set(range(variables_count, variables_count + equations_count))
    print("Initial basis:", basis)

    # Append a bunch of zeroes to vector C for each artificial variable
    c = array([*c, *[0] * equations_count])

    # Compute bounds for artificial variables
    for lefthand, righthand, sign in zip(A, b, signs):
        lefthand_extremum = sum(
            coeff * vbounds[sign * coeff > 0] for coeff, vbounds in zip(lefthand, bounds)
        )
        new_bound = [0, (lefthand_extremum - righthand) * sign]
        new_bound.sort()
        bounds.append(new_bound)
    print("Bounds:", bounds)

    # Append identity matrix to A
    A = matrix(append(A, eye(equations_count), axis=1))

    return c, A, b, bounds, basis


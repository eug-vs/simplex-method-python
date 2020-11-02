import simplex
from test_data import problems
from numpy import matrix


for problem in problems:
    print("Problem:")
    print("c =", problem["c"])
    print(matrix(problem["A"]))
    print("b =", problem["b"])

    expected_result = problem.pop("expected_result")

    result = simplex.solve(**problem)

    assert all((result - expected_result) < 0.01), f"Result should be {expected_result}"
    print("Result is correct!\n\n")


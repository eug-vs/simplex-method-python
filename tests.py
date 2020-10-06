import simplex
from test_data import data
from numpy import matrix


for problem in data:
    print("Problem:")
    print("c =", problem["c"])
    print(matrix(problem["A"]))
    print("b =", problem["b"])

    expected_result = problem.pop("expected_result")
    if "basis" not in problem:
        problem = simplex.to_standart_form(**problem)

    result = simplex.solve(**problem)

    assert all((result - expected_result) < 0.01), f"Result should be {expected_result}"
    print("Result is correct!\n\n")


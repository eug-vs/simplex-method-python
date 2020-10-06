from numpy import inf


data = [
    {
        "c": [4, 1],
        "A": [
            [-4, 3],
            [2, 3],
        ],
        "b": [12, 30],
        "signs": [-1, -1],
        "bounds": [(0, 6), (0, inf)],
        "expected_result": [6, 6, 18, 0]
    },
    {
        # Already in standart form, provided with basis instead of signs
        "c": [2, 1, 0, 0, 0],
        "A": [
            [-1, 1, 1, 0, 0],
            [1, -2, 0, 1, 0],
            [4, 1, 0, 0, 1],
        ],
        "b": [3, 6, 22],
        "basis": { 2, 3, 4 },
        "bounds": [(0, 5), (0, 4), (0, 8), (0, 14), (0, 22)],
        "expected_result": [4.5, 4, 3.5, 9.5, 0]
    },
    {
        "c": [5, 3],
        "A": [
            [1, 1],
            [5, 2],
        ],
        "b": [4, 10],
        "signs": [-1, -1],
        "bounds": [(0, inf), (0, inf)],
        "expected_result": [2/3, 10/3, 0, 0]
    },
    {
        "c": [4, 6],
        "A": [
            [2, 1],
            [1, 3],
        ],
        "b": [64, 72],
        "signs": [-1, -1],
        "bounds": [(0, inf), (0, 20)],
        "expected_result": [24, 16, 0, 0]
    },
]

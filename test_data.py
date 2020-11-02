from numpy import inf


problems = [
    {
        "c": [-2, 0, 0, 5, -4],
        "A": [
            [-4, 1, 0, 0, 3],
            [2, 0, 0, 0, -1],
            [0, 0, 2, 1, 0],
        ],
        "b": [6, -2, 6],
        "bounds": [
            [0, 4],
            [-1, 4],
            [0, 5],
            [-2, 3],
            [0, 6],
        ],
        "expected_result": [0, 0, 1.5, 3, 2]
    },
    {
        "c": [-4, 8, 8, 0, -3],
        "A": [
            [-1, 0, 0, 0, 3],
            [0, 2, 4, 0, 0],
            [0, 1, 0, 3, 2],
        ],
        "b": [-1, 24, 6],
        "bounds": [
            [1, 6],
            [1, 6],
            [0, 4],
            [-2, 3],
            [-1, 4],
        ],
        "expected_result": [1, 6, 3, 0, 0]
    }
]

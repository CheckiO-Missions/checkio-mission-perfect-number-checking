"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {"input": [6], "answer": True},
        {"input": [2], "answer": False},
        {"input": [28], "answer": True},
        {"input": [20], "answer": False},
        {"input": [496], "answer": True},
        {"input": [30], "answer": False},
        {"input": [8128], "answer": True},
        {"input": [100], "answer": False},
        {"input": [500], "answer": False},
        {"input": [1000], "answer": False}
    ],
    "Extra": [
        {"input": [33550336], "answer": True},  # This is the next perfect number after 8128
        {"input": [999983], "answer": False}
    ]
}

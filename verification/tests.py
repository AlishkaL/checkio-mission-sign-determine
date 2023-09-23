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
        {"input": [5], "answer": "positive"},
        {"input": [0], "answer": "zero"},
        {"input": [-10], "answer": "negative"},
        {"input": [1], "answer": "positive"},
        {"input": [-1], "answer": "negative"},
        {"input": [999], "answer": "positive"},
        {"input": [-1000], "answer": "negative"},
        {"input": [123456789], "answer": "positive"},
        {"input": [-987654321], "answer": "negative"},
        {"input": [2], "answer": "positive"}
    ],
    "Extra": [
        {"input": [2**31 - 1], "answer": "positive"},
        {"input": [-2**31 + 1], "answer": "negative"}
    ]
}

"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": u"SEND MORE MONEY",
            "answer": True,
        },
        {
            "input": u"GET LESS JOBS",
            "answer": True,
        },
        {
            "input": u"I LOVE YOU",
            "answer": False,
        },
        {
            "input": u"RAINS DOGS CATS",
            "answer": False,
        },
        {
            "input": u"TIME IS MONEY",
            "answer": False,
        },
    ]
}

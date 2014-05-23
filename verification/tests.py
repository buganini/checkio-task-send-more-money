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
            "input": u"AAA BBB CCC",
            "answer": True,
        },
        {
            "input": u"AAA AAA AAA",
            "answer": False,
        },
        {
            "input": u"NO ANSWER HERE",
            "answer": False,
        },
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
        {
            "input": u"ONE ONE TWO",
            "answer": True,
        },
        {
            "input": u"ONE TWO THREE",
            "answer": False,
        },
        {
            "input": u"TOP AND DOWN",
            "answer": True,
        },
        {
            "input": u"HOW ARE YOU",
            "answer": True,
        },
        {
            "input": u"AND OR NOT",
            "answer": True,
        },
        {
            "input": u"PYCON APAC TAIWAN",
            "answer": False,
        },
    ]
}

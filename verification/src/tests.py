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
        {
            "input": "some text",
            "answer": "... --- -- .   - . -..- -"
        },
        {
            "input": "I was born in 1990",
            "answer": "..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----"
        }
    ],
    "Extra": [
        {
            "input": "abcdefghijklmnopqrstuvwxyz",
            "answer": ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
        },
        {
            "input": "0123456789 are digits",
            "answer": "----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.   .- .-. .   -.. .. --. .. - ..."
        },
	{
            "input": "v3ry 10ng str1ng w1th s0m3 numb3r5",
            "answer": "...- ...-- .-. -.--   .---- ----- -. --.   ... - .-. .---- -. --.   .-- .---- - ....   ... ----- -- ...--   -. ..- -- -... ...-- .-. ....."
        }
    ]
}

"""Convert a non-negative integer into its spoken language form

Usage:
>>> convert_to_spoken(1)
'one'

Running tests:
$ mkvirtualenv dimagi
$ pip install nose
$ nosetests
"""

class Error(Exception): pass

def convert_to_spoken(number):
    """Convert a non-negative integer into its spoken language form

    This implementation can convert every number between negative one
    (-1) and one quadrillion, non-inclusive.

    :param number: An integer.
    :returns: A string.
    :raises: Error if the given number could not be converted.
    """
    if not isinstance(number, int):
        raise Error("not a number")
    if number < 0:
        raise Error("number must be non-negative")

    words = []
    for power, word in powers:
        if number >= 10 ** power:
            num, number = divmod(number, 10 ** power)
            if num >= 1000:
                raise Error("number is too large")
            words.append(convert_to_spoken(num))
            words.append(word)

    assert number < 100, number
    if number > 0 or not words:
        try:
            words.append(table[number])
        except KeyError:
            assert number > 20, number
            tens, number = divmod(number, 10)
            words.append(table[tens * 10])
            words.append(table[number])
    return " ".join(words)

table = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

powers = [
    (12, "trillion"),
    (9, "billion"),
    (6, "million"),
    (3, "thousand"),
    (2, "hundred"),
]


def test_spoken():
    def test(number, spoken):
        eq_(convert_to_spoken(number), spoken)

    yield test, 0, "zero"
    yield test, 1, "one"
    yield test, 2, "two"
    yield test, 3, "three"
    yield test, 4, "four"
    yield test, 5, "five"
    yield test, 6, "six"
    yield test, 7, "seven"
    yield test, 8, "eight"
    yield test, 9, "nine"
    yield test, 10, "ten",
    yield test, 11, "eleven"
    yield test, 12, "twelve"
    yield test, 13, "thirteen"
    yield test, 14, "fourteen"
    yield test, 15, "fifteen"
    yield test, 16, "sixteen"
    yield test, 17, "seventeen"
    yield test, 18, "eighteen"
    yield test, 19, "nineteen"

    yield test, 20, "twenty"
    yield test, 21, "twenty one"
    yield test, 22, "twenty two"
    yield test, 23, "twenty three"
    yield test, 24, "twenty four"
    yield test, 25, "twenty five"
    yield test, 26, "twenty six"
    yield test, 27, "twenty seven"
    yield test, 28, "twenty eight"
    yield test, 29, "twenty nine"

    yield test, 30, "thirty"
    yield test, 35, "thirty five"
    yield test, 39, "thirty nine"

    yield test, 40, "forty"
    yield test, 45, "forty five"
    yield test, 49, "forty nine"

    yield test, 50, "fifty"
    yield test, 55, "fifty five"
    yield test, 59, "fifty nine"

    yield test, 60, "sixty"
    yield test, 65, "sixty five"
    yield test, 69, "sixty nine"

    yield test, 70, "seventy"
    yield test, 75, "seventy five"
    yield test, 79, "seventy nine"

    yield test, 80, "eighty"
    yield test, 85, "eighty five"
    yield test, 89, "eighty nine"

    yield test, 90, "ninety"
    yield test, 95, "ninety five"
    yield test, 99, "ninety nine"

    yield test, 100, "one hundred"
    yield test, 101, "one hundred one"
    yield test, 102, "one hundred two"
    yield test, 108, "one hundred eight"
    yield test, 109, "one hundred nine"
    yield test, 110, "one hundred ten"
    yield test, 111, "one hundred eleven"
    yield test, 119, "one hundred nineteen"

    yield test, 120, "one hundred twenty"
    yield test, 121, "one hundred twenty one"

    yield test, 130, "one hundred thirty"
    yield test, 132, "one hundred thirty two"

    yield test, 140, "one hundred forty"
    yield test, 143, "one hundred forty three"

    yield test, 150, "one hundred fifty"
    yield test, 154, "one hundred fifty four"

    yield test, 160, "one hundred sixty"
    yield test, 165, "one hundred sixty five"

    yield test, 170, "one hundred seventy"
    yield test, 176, "one hundred seventy six"

    yield test, 180, "one hundred eighty"
    yield test, 187, "one hundred eighty seven"

    yield test, 190, "one hundred ninety"
    yield test, 198, "one hundred ninety eight"
    yield test, 199, "one hundred ninety nine"

    yield test, 200, "two hundred"
    yield test, 210, "two hundred ten"
    yield test, 299, "two hundred ninety nine"

    yield test, 300, "three hundred"
    yield test, 320, "three hundred twenty"
    yield test, 399, "three hundred ninety nine"

    yield test, 3000, "three thousand"
    yield test, 4589, "four thousand five hundred eighty nine"
    yield test, 42589, "forty two thousand five hundred eighty nine"
    yield test, 427589, (
        "four hundred twenty seven thousand five hundred eighty nine")

    yield test, 3000001, "three million one"
    yield test, 4000000001, "four billion one"
    yield test, 5000000000001, "five trillion one"
    yield test, 999999999999999, (
        "nine hundred ninety nine trillion "
        "nine hundred ninety nine billion "
        "nine hundred ninety nine million "
        "nine hundred ninety nine thousand "
        "nine hundred ninety nine"
    )


def test_errors():
    def test(number, message):
        try:
            print(convert_to_spoken(number))
            raise AssertionError("error not raised: {}".format(message))
        except Error as err:
            eq_(str(err), message)

    yield test, "100", "not a number"
    yield test, [1], "not a number"
    yield test, -100, "number must be non-negative"
    yield test, -1, "number must be non-negative"
    yield test, 1000000000000000, "number is too large"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test helpers

def eq_(a, b, message=None):
    assert a == b, (message or "{} != {}".format(a, b))

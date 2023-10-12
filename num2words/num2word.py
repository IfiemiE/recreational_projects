#!/usr/bin/python3
""" This module contains functions for naming numbers in words"""


def zero(num):
    """ A function for handling zero as a special case"""

    num = int(num)
    if num == 0:
        return ("Zero")


def one_digit(num):
    """ A function for naming single digit numbers apart from zero"""

    num = int(num)
    if (0 < num) and (num <= 9):
        names = ["One", "Two", "Three", "Four", "Five",
                        "Six", "Seven", "Eight", "Nine"]
        num = int(num)
        return (names[num - 1])


def two_digit(num):
    """ A function for naming double digit numbers
    Degenerates to one_digit function if number begins with a zero
    """
    num = int(num)
    if (0 < num) and (num <= 99):
        if (num <= 9):
            return (one_digit(num))
        elif (9 < num) and (num <= 19):
            names1 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
                      "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                      "Nineteen"]
            return (names1[num - 10])
        else:
            names2 = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty",
                      "Seventy", "Eighty", "Ninety"]
            tens = num // 10
            unit = num % 10
            if (unit == 0):
                return (names2[tens - 2])
            else:
                return ("{} {}".format(names2[tens - 2], one_digit(unit)))


def three_digit(num):
    """A function for naming three digit numbers
    Degenerates to two_digit function if number begins with a zero
    """
    num = int(num)
    if (0 < num) and (num <= 999):
        if (num <= 99):
            return (two_digit(num))
        else:
            hun = num // 100
            tens_unit = num % 100
            if (tens_unit == 0):
                return ("{} Hundred".format(one_digit(hun)))
            else:
                return ("{} Hundred and {}".format(one_digit(hun),
                        two_digit(tens_unit)))


def group3(num):
    """A function for splitting digits into groups of threes
    Removes all zero prefixes
    """
    groups = []
    b = len(num)
    a = b - 3
    while (a >= 0):
        groups.insert(0, num[a:b])
        a -= 3
        b -= 3
    if (a < 0) and (b > 0):
        groups.insert(0, num[0:b])

    while (int(groups[0]) == 0) and (len(groups) != 1):
        groups.pop(0)
    while groups[0][0] == '0' and len(groups[0]) != 1:
        groups[0] = groups[0][1:]

    if int(groups[0]) == 0:
        groups = ['0']
    return (groups)


def more_digit(num):
    """ A function to name numbers with more than three digits
    -Splits the number into groups of 3's
    -Names each groups
    -Degenerates to three_digit function for a group beginning with zero
    """
    parts = group3(num)
    np = len(parts)
    marked_num = ""
    for mn in range(np):
        if mn != (np - 1):
            marked_num += "{},".format(parts[mn])
        else:
            marked_num += parts[mn]
    print(marked_num)

    if (np == 1) and int(parts[0]) == 0:
        return (zero(num))
    names3 = [None, "Thousand", "Million", "Billion", "Trillion",
              "Quadrillion", "Quintillion", "Sixtillion", "Septillion",
              "Octillion", "Nonillion", "Decillion"]
    words = ""
    for i in range(np):
        hun = three_digit(parts[i])
        j = (np - 1) - i
        if j > len(names3) - 1:
            print(f"For No more than {3*len(names3)} digits:
                  Increase the place value list")
            return
        if (hun is not None):
            if (names3[j] is None):
                words += hun
            else:
                for c in range(i + 1, np):
                    if (int(parts[c]) != 0):
                        words += "{} {}, ".format(hun, names3[j])
                        break
                else:
                    words += "{} {}".format(hun, names3[j])
    return (words)


if __name__ == '__main__':
    import sys
    for i in range(1, len(sys.argv)):
        num = sys.argv[i]
        if num.isdigit():
            word = more_digit(num)
            print("{}".format(word))

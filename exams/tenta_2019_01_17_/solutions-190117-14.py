# Detta Ã¤r en uppsÃ¤ttning lÃ¶sningsfÃ¶rslag fÃ¶r en tenta i TDDE24.

# LÃ¶sningsfÃ¶rslagen saknar docstrings, vilket krÃ¤vs fÃ¶r full poÃ¤ng!

# I vissa fall ges flera lÃ¶sningsfÃ¶rslag, och till och med exempel pÃ¥
# felaktiga lÃ¶sningar.


import sys

from helpers import *


# ======================================================================
# Uppgift 1

# This short solution uses the built-in min/max functions.
# To do this properly you need to use default=None,
# otherwise min/max will not work when seq is empty.
def minpos_maxneg(seq):
    min_pos = min([x for x in seq if x > 0], default=None)
    max_neg = max([x for x in seq if x < 0], default=None)
    return min_pos, max_neg


# A working solution without list comprehensions,
# explicitly iterating over the sequence.
def minpos_maxneg2(seq):
    min_pos = None
    max_neg = None
    for x in seq:
        if x < 0:
            if max_neg is None or x > max_neg:
                max_neg = x
        elif x > 0:
            if min_pos is None or x < min_pos:
                min_pos = x

    return min_pos, max_neg


# ======================================================================
# Uppgift 2


def sum_pairs_i(seq):
    if not seq:
        return []
    elif len(seq) == 1:
        return seq
    else:
        result = []
        for index in range(len(seq) - 1):
            result += [seq[index] + seq[index + 1]]
        return result


def sum_pairs_r(seq):
    if not seq:
        return []
    elif len(seq) == 1:
        return seq
    elif len(seq) == 2:
        # Must have another base case to terminate here.
        # If you use the default case, you'll get an extra number at the end
        # due to the recursion.
        return [seq[0] + seq[1]]
    else:
        return [seq[0] + seq[1]] + sum_pairs_r(seq[1:])


# ======================================================================
# Uppgift 3


def power_of_each(lst):
    result = []
    for element in lst:
        if isinstance(element, list):
            # Call power_of_each recursively for the inner list
            # The result is a list that we append
            result.append(power_of_each(element))
        else:
            result.append(2 ** element)
    return result


# ======================================================================
# Uppgift 4

def multiple_apply(f, n):
    def n_times(start):
        result = start
        for i in range(n):
            result = f(result)
        return result

    return lambda val: n_times(val)


# 4b: A single expression.
pow2mult = lambda n, c: multiple_apply(lambda x: 2*x, n)(c)


# ======================================================================
# Uppgift 5

def can_interleave(part1, part2, whole):

    if not part1 and not part2 and not whole:
        # We have consumed both parts in an order that consumed all of whole.
        return True

    elif part1 and whole and part1[0] == whole[0] and can_interleave(part1[1:], part2, whole[1:]):
        # part1 is non-empty, and so is whole.
        # part1 begins with the same character as whole.
        # If we remove those two (identical) characters, we can interleave the remainder as well,
        return True

    elif part2 and whole and part2[0] == whole[0] and can_interleave(part1, part2[1:], whole[1:]):
        # Like above, but for part 2.
        return True

    else:
        return False


# This version is wrong: If part1[0] == whole[0], it decides directly that the
# next character MUST be taken from part1, even though it could also have been
# taken from part2.  If you can't interleave after taking the character from
# part1, but you COULD have interleaved after taking it from part2, this fails.
# Example: can_interleave_wrong("abc", "add", "addabc") == False, because
# the function only considers taking "a" from "abc" and is then unable to find
# a "d" for the next character in "addabc".

def can_interleave_wrong(part1, part2, whole):

    if not part1 and not part2 and not whole:
        # We have consumed both parts in an order that consumed all of whole.
        return True

    elif part1 and whole and part1[0] == whole[0]:
        if can_interleave_wrong(part1[1:], part2, whole[1:]):
            return True

    elif part2 and whole and part2[0] == whole[0]:
        if can_interleave_wrong(part1, part2[1:], whole[1:]):
            return True

    return False


# The version below works, but does not really have a strict recursive structure:
# Instead of recursing to solve subproblems and *then* accumulating the answer,
# it incrementally builds up a string in so_far, which is similar to an iterative
# solution.  It is also less efficient as it does not check whether the way it
# picks characters has any chance of actually resulting "whole" until it has actually
# taken ALL characters.  If you check can_interleave_2("abc", "def", "xyz123"), then
# it will construct ALL interleavings such as "abcdef", "abdecf" and so on.  The first
# version above would immediately see that neither "a" nor "d" matched "x".
def can_interleave_2(part1, part2, whole, so_far=""):

    if not part1 and not part2:
        # There are no characters left in any of the parts.
        return so_far == whole

    elif part1 and can_interleave_2(part1[1:], part2, whole, so_far + part1[0]):
        return True

    elif part2 and can_interleave_2(part1, part2[1:], whole, so_far + part2[0]):
        return True

    else:
        return False


# ======================================================================
# Uppgift 6

def las(a1, n):
    current = a1
    result = []

    # Do it n times.  (This is actually somewhat inefficient since we only
    # need 1 copy of the original number and n-1 "transformations".)
    for i in range(n):
        result.append(current)
        as_string = str(current)  # A string such as "1112"
        numstring = ""

        # For each character in the string such as "1112"
        while as_string:
            # Now we have at least 1 digit
            first = as_string[0]
            count = 1

            # Do we have more identical digits at the start (such as three '1' characters)?
            while count < len(as_string) and as_string[count] == first:
                count += 1

            # In the example: count==3, first==1
            numstring += str(count) + str(first)

            # Skip the digits we just used
            as_string = as_string[count:]

        # Convert the resulting string (such as "3112") to a number again.
        current = int(numstring)

    return result

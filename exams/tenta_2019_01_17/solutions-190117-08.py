# Detta Ã¤r en uppsÃ¤ttning lÃ¶sningsfÃ¶rslag fÃ¶r en tenta i TDDE24.

# LÃ¶sningsfÃ¶rslagen saknar docstrings, vilket krÃ¤vs fÃ¶r full poÃ¤ng!

# I vissa fall ges flera lÃ¶sningsfÃ¶rslag, och till och med exempel pÃ¥
# felaktiga lÃ¶sningar.


# ======================================================================
# Uppgift 1

# This short solution uses the built-in min/max functions.
# To do this properly you need to use default=None,
# otherwise min/max will not work when seq is empty.
def minodd_maxeven(seq):
    min_odd = min([x for x in seq if x % 2 == 1], default=None)
    max_even = max([x for x in seq if x % 2 == 0], default=None)
    return min_odd, max_even


# This non-solution illustrates a possible error.
def minodd_maxeven2_faulty(seq):
    min_odd = None
    max_even = None
    for x in seq:
        if x % 2 == 0:
            # Error in test below:  0 counts as false,
            # so we can't test "if we haven't had
            # an even number yet" using "not max_even"!
            if not max_even or x > max_even:
                max_even = x
        else:
            if not min_odd or x < min_odd:
                min_odd = x

    return min_odd, max_even


# A working solution without list comprehensions,
# explicitly iterating over the sequence.
def minodd_maxeven2(seq):
    min_odd = None
    max_even = None
    for x in seq:
        if x % 2 == 0:
            if max_even is None or x > max_even:
                max_even = x
        else:
            if min_odd is None or x < min_odd:
                min_odd = x

    return min_odd, max_even


# ======================================================================
# Uppgift 2

def skiplist_i(seq):
    result = []

    while seq:
        count = seq[0]
        result += [count]
        seq = seq[count + 1:]

    return result


def skiplist_r(seq):
    if not seq:
        return []

    else:
        count = seq[0]
        # Here we skip all elements in a single leap,
        # using seq[count + 1:].
        #
        # This is fine even in a recursive solution.
        # An alternative would be to recurse once for every
        # element to skip.
        return [count] + skiplist_r(seq[count + 1:])


# ======================================================================
# Uppgift 3

def length_of_each(lst):
    result = []
    for element in lst:
        if isinstance(element, list):
            # Call length_of_each recursively for the inner list
            # The result is a list that we append
            result.append(length_of_each(element))
        else:
            result.append(len(element))
    return result


# ======================================================================
# Uppgift 4


def pairwise_apply(f):
    def pairwise(l1, l2):
        result = []
        # For all indexes where we have elements in both l1 and l2...
        for index in range(min(len(l1), len(l2))):
            result.append(f(l1[index], l2[index]))
        return result

    return lambda l1, l2: pairwise(l1, l2)


# Alternative: Use the zip function to combine elements from lists,
# and *pair to "split" the pair into separate parameters
def pairwise_apply_2(f):
    def pairwise(l1, l2):
        result = []
        for pair in zip(l1, l2):
            result.append(f(*pair))
        return result

    return lambda l1, l2: pairwise(l1, l2)


# 4b: A single expression.
pairwise_multiply = pairwise_apply(lambda e1, e2: e1 * e2)


# ======================================================================
# Uppgift 5


def can_break_lines(words, minlen, maxlen):
    # If we've reached the end, everything is fine
    if not words:
        return True

    # Otherwise, we need to construct a line from *some* prefix of the word list,
    # this line must have the right length,
    # and it must be possible to continue according to the definition.

    # Note that we do have to check different prefixes of the list.
    # There may be more than one prefix that works for *this* line,
    # but the choice we make here will also affect whether we can break
    # the *remaining* lines in a way that satisfies the rules.

    # Here we test all possible prefixes of words, including ones that
    # are definitely too long.  This could be optimized, but is left
    # as it is for clarity.
    for index in range(1, len(words) + 1):
        # Construct the actual line
        currline = " ".join(words[:index])
        # Check that this line satisfies requirements AND that we can
        # then continue...
        if minlen <= len(currline) <= maxlen and can_break_lines(words[index:], minlen, maxlen):
            return True

    return False


# This implementation is somewhat more efficient, since it does not
# check lines that exceed the maximum length.  It also has a different
# structure.
def can_break_lines_more_efficient(words, minlen, maxlen):
    if not words:
        return True

    # Since there are words left, the current line must contain at least one word
    currline = words[0]

    # Must at least add enough words to reach reach minlen
    pos = 1
    while len(currline) < minlen and pos < len(words):
        currline += " " + words[pos]
        pos += 1

    # Now it's sufficient to add words until we exceed maxlen
    while len(currline) <= maxlen:
        # Now currline satisfies the requirements, but can we then also
        # find a solution for the remainder of the words?
        worked = can_break_lines_more_efficient(words[pos:], minlen, maxlen)
        if worked:
            return True

        # Are there words left to add to this line?  If not, give up.
        if pos >= len(words):
            break

        # OK, let's see if another word will fit
        currline += " " + words[pos]
        pos += 1

    return False


# As above, but returns the resulting lines as well.
def can_break_lines_with_result(words, minlen, maxlen):
    if not words:
        return True, []

    currline = words[0]

    # Must at least reach minlen
    pos = 1
    while len(currline) < minlen and pos < len(words):
        currline += " " + words[pos]
        pos += 1

    if len(currline) < minlen:
        return False, None

    while len(currline) <= maxlen:
        # Can we break here?
        worked, result = can_break_lines_with_result(words[pos:], minlen, maxlen)
        if worked:
            return True, [currline] + result

        # OK, let's see if another word will fit
        currline += " " + words[pos]
        pos += 1

    return False, None


# ======================================================================
# Uppgift 6

def golomb(n):
    result = []
    current = 1
    times_added = 0

    for i in range(1, n + 1):
        # We need to append the current value
        result.append(current)
        times_added += 1

        # Have we appended the current value the correct number of times?

        # List indexes start at 0, and Golomb sequence indexes start at 1.
        # That's why we use result[current-1] instead of result[current].
        if times_added == result[current - 1]:
            # OK, time to step to the next value.
            current += 1
            times_added = 0

    return result

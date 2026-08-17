from typing import NamedTuple, Any


def invert_dict(d: dict) -> dict:
    inverted = {}
    for key, value in d.items():
        if value not in inverted.keys():
            inverted[value] = []
        inverted[value] += [key]

    return inverted


# def is_mountain(seq: list[int]) -> bool:
#     if len(seq) < 3:
#         return False

#     has_increased = False
#     has_decreased = False

#     for i in range(len(seq) - 1):
#         a = seq[i]
#         b = seq[i + 1]

#         if a == b:
#             return False

#         if a < b:
#             if has_decreased:
#                 return False

#             has_increased = True
#         else:
#             has_decreased = True

#     return has_increased and has_decreased


def is_mountain(seq: list[int]) -> bool:
    if len(seq) < 3:
        return False

    top = max(seq)
    top_index = seq.index(top)

    if top_index == 0 or top_index == len(seq) - 1:
        return False

    for i in range(0, top_index):
        if seq[i] >= seq[i+1]:
            return False

    for i in range(top_index, len(seq) - 1):
        if seq[i] <= seq[i+1]:
            return False

    return True


def enumerate_nested(nest: list) -> dict:
    result = {}

    def help_fuc(current_list, path):
        for i, item in enumerate(current_list):
            new_path = path + (i, )
            if isinstance(item, list):
                help_fuc(item, new_path)
            else:
                result[new_path] = item
    help_fuc(nest, ())
    return result


def make_validator(rules: list):
   def validator(value):
       for rule in rules:
           if not rule(value):
               return False
       return True
   return validator

def filter_valid(seq: list, validator_func) -> list:
    return [ num for num in seq if validator_func(num)]


def crosses_own_path(moves: str) -> bool:
    x = 0
    y = 0
    visited = set({(0, 0)})

    for move in moves:
        if move == "N":
            y += 1
        elif move == "E":
            x += 1
        elif move == "S":
            y -= 1
        elif move == "W":
            x -= 1
 
        position = (x, y)

        if position in visited:
            return True

        visited.add(position)

    return False


class ListSet(NamedTuple): elements: list[Any]

def new_listset() -> ListSet:
    return ListSet([])

def listset_add(ls: ListSet, val: Any) -> None:
    if val not in ls.elements:
        ls.elements.append(val)

def listset_contains(ls: ListSet, val: Any):
    return True if val in ls.elements else False

def listset_union(ls1: ListSet, ls2: ListSet):
    new_set = new_listset()
 
    for val in [*ls1.elements, *ls2.elements]:
        if val not in new_set.elements:
            new_set.elements.append(val)

    return new_set
    
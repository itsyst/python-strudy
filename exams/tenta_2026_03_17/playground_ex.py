import re


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
    if len(seq) <3:
        return False

    top = max(seq)
    top_index = seq.index(top)

    if top_index == 0 or top_index == len(seq) -1:
        return False
    
    for i in range(0, top_index):
        if seq[i] >= seq[i+1]:
            return False

    for i in range(top_index, len(seq) -1):
        if seq[i] <= seq[i+1]:
            return False 

    return True
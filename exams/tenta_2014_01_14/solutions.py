# encoding: iso-8859-1

# -----------------------------------------------------------------------------
#  Datortentamen i kursen TDDD73 Funktionell och imperativ programmering i Python
#  2014-01-14
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#  Uppgift 1
# -----------------------------------------------------------------------------

def find_notes(str):
    result = ""
    for char in str:
        if char in "cdefgahCDEFGAH":
            result += char.lower()
    return result

def print_notes(str):
    for note in "hagfedc":
        line = ""
        for char in str:
            if char == note:
                line += note
            else:
                line += '.'
        print(line)

# -----------------------------------------------------------------------------
#  Uppgift 2
# -----------------------------------------------------------------------------

def merge_r(seq1, seq2):
	if not seq1:
		return seq2
	elif not seq2:
		return seq1
	elif seq1[0] < seq2[0]:
		return [seq1[0]] + merge_r(seq1[1:], seq2)
	else:
		return [seq2[0]] + merge_r(seq1, seq2[1:])
		
def merge_i(seq1, seq2):
	res = []
	while seq1 and seq2:
		if seq1[0] < seq2[0]:
			res.append(seq1[0])
			seq1 = seq1[1:]
		else:
			res.append(seq2[0])
			seq2 = seq2[1:]
	res = res + seq1 + seq2
	return res
	
# -----------------------------------------------------------------------------
#  Uppgift 3
# -----------------------------------------------------------------------------

def insert(element, seq, order_fn):
    if not seq:
        return [element]
    elif order_fn(seq[0], element):
        return [seq[0]] + insert(element, seq[1:], order_fn)
    else:
        return [element] + seq

def insert_abs(element, seq):
    return insert(element, seq, lambda x, y: abs(x) < abs(y))

def insert_seq(subseq, seq):
    return insert(subseq, seq, lambda x, y: len(x) > len(y))

# -----------------------------------------------------------------------------
#  Uppgift 4
# -----------------------------------------------------------------------------

def longest_sequence(seq):
    def longest_sequence_help(seq, cur_elm, cur_cnt, tot_elm, tot_cnt):
        if not seq:
            if cur_cnt > tot_cnt:
                return cur_elm, cur_cnt
            else:
                return tot_elm, tot_cnt
        elif seq[0] == cur_elm:
            return longest_sequence_help(seq[1:], cur_elm, cur_cnt+1, tot_elm, tot_cnt)
        elif cur_cnt > tot_cnt:
            return longest_sequence_help(seq, seq[0], 0, cur_elm, cur_cnt)
        else:
            return longest_sequence_help(seq, seq[0], 0, tot_elm, tot_cnt)   
    return longest_sequence_help(seq, seq[0], 0, 'NONE', 0)

# -----------------------------------------------------------------------------
#  Uppgift 5
# -----------------------------------------------------------------------------

children = {'Linus': ('Eva', 'Per'),
            'Linnea': ('Per', ),
            'Eva': ('Emilia', 'Emil'),
            'Per': ('Stina', ),
            'Stina': ('Lillan', )}
            
def descendants(person, table):
    result = []
    if person in table:
        children = table[person]
        result = list(children)
        for child in children:
            result += descendants(child, table)
    return result
    
# -----------------------------------------------------------------------------
#  Uppgift 6
# -----------------------------------------------------------------------------

from discrim_s import *

def is_fact(obj):
    "object -> truth value"
    return isinstance(obj, list) and obj[0] == "FACT"
    
def item(f, level):
    "fact x integer -> item"
    return f[level]

def discriminate(f1, f2, level):
    "fact x fact x integer -> d_tree"
    if item(f1, level) == item(f2, level):
        return extend_branch_seq(build_branch(item(f1, level), discriminate(f1, f2, level+1)), 
                                 empty_branch_seq())
    else:
        return extend_branch_seq(build_branch(item(f1, level), f1),
                 extend_branch_seq(build_branch(item(f2, level), f2), empty_branch_seq()))

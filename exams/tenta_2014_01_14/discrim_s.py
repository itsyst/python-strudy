
# ----- Discrimination trees -----

def insert_dt(dt, fact):
    "d_tree x fact -> d_tree"
    if is_empty_dt(dt):
        return fact
    else:
        return insert_dt_at(dt, fact, 1)
        
def insert_dt_at(dt, fact, level):
    "d_tree x fact x integer -> d_tree"
    if is_fact(dt):
        return discriminate(dt, fact, level)
    else:
        return insert_aux(dt, item(fact, level), fact, level)
        
def insert_aux(br_seq, fact_discr, fact, level):
    "d_tree x item x fact x integer -> d_tree"
    if is_empty_branch_seq(br_seq):
        return extend_branch_seq(build_branch(fact_discr, fact), empty_branch_seq())
    elif branch_item(first_branch(br_seq)) == fact_discr:
        return extend_branch_seq(build_branch(branch_item(first_branch(br_seq)), 
                                              insert_dt_at(branch_seq(first_branch(br_seq)), fact, level+1)), 
                                 rest_branches(br_seq))
    else:
        return extend_branch_seq(first_branch(br_seq), insert_aux(rest_branches(br_seq), fact_discr, fact, level))
        
#def discriminate(f1, f2, level):
#    "fact x fact x integer -> d_tree"
#    # *** To be definied in assignment 6b ***
    
# ----- Primitives for the fact datatype -----

#def is_fact(obj):
#    "object -> truth value"
#    # *** To be definied in assignment 6a ***
    
#def item(f, level):
#    "fact x integer -> item"
#    # *** To be definied in assignment 6a ***
    
def build_fact(seq):
    "list of items -> fact"
    return ["FACT"] + seq
    
# ----- Primitives for the branch datatype -----

def build_branch(i, dt):
    "item x branch_seq -> branch"
    return [i, dt]
    
def branch_item(br):
    "branch -> item"
    return br[0]
    
def branch_seq(br):
    "branch -> branch_seq"
    return br[1]
    
# ----- Primitives for the branch_seq/d_tree datatypes -----

def extend_branch_seq(br, br_seq):
    "branch x branch_seq -> branch_seq"
    return [br] + br_seq
    
def first_branch(br_seq):
    "branch_seq -> branch"
    return br_seq[0]
    
def rest_branches(br_seq):
    "branch_seq -> branch_seq"
    return br_seq[1:]

def empty_branch_seq():
    "-> branch_seq"
    return []
    
def is_empty_branch_seq(br_seq):
    "branch_seq -> truth value"
    return not br_seq
    
def build_tree(br, br_seq):
    "branch x branch_seq -> d_tree"
    return [br] + br_seq
    
def is_empty_dt(dt):
    "d_tree -> truth value"
    return not dt
    
# ----- Tests -----

fact1 = build_fact(["far", "Per", "Lisa"])
fact2 = build_fact(["mor", "Stina", "Lisa"])
fact3 = build_fact(["far", "Per", "Nils"])

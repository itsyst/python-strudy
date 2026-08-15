

"""

  Ã–versikt Ã¶ver vÃ¥ra abstrakta datatyper:

  word = en strÃ¤ng

  sentence = [word, ...]

  category = en strÃ¤ng

  category sequence = [category, ...]
  
  lexicon entry = <word, category sequence>

  lexicon = [lexicon entry, ...]

  rule = <category, category sequence>

  grammar = [rule, ...]

"""

# ----- Datatypen word -----

# Datatypen word representerar ett ord sÃ¥ som det fÃ¶rekommer i ett lexikon eller
# i en mening. Det lagras som en vanlig strÃ¤ng och inga extra primitiva funktioner
# behÃ¶vs.

# ----- Datatypen sentence -----

# Datatypen senctence representerar en mening och Ã¤r i grund och botten en sekvens
# av ord. I detta exempel skapas meningarna frÃ¤mst av funktionen generate. De lagras
# som listor, men har ett antal primitiva funktioner.

def create_sencente():
  "-> sentence"
  return []
  
def add_word(word, sent):
  "word x sentence -> sentence"
  return sent + [word]
  
def append_sentences(sent1, sent2):
  "sentence x sentence -> sentence"
  return sent1 + sent2

# ----- Datatypen category -----

# Datatypen category representerar en kategori sÃ¥ som den fÃ¶rekommer i ett lexikon
# eller i en grammatisk regel. Den lagras som en vanlig strÃ¤ng och inga extra
# primitiva funktioner behÃ¶vs.

# ----- Datatypen category sequence -----

# Datatypen category sequence representerar en sekvens av kategorier. Den fÃ¶rekommer
# som hÃ¶gra delen av en rad i ett lexikon, samt som hÃ¶gra delen av en grammatisk
# regel. En category sequence (fÃ¶rkortad cat_seq) lagras som en lista och har ett
# antal primitiva funktioner associerade.

def create_cat_seq():
  "-> category sequence"
  return []
  
def add_category(cat, cat_seq):
  "category x category sequence -> category sequence"
  return [cat] + cat_seq
  
def first_category(cat_seq):
  "category sequence -> category"
  return cat_seq[0]
  
def rest_cat_seq(cat_seq):
  "category sequence -> category sequence"
  return cat_seq[1:]
  
def is_empty_cat_seq(cat_seq):
  "category sequence -> truth value"
  return not cat_seq
  
def category_in_cat_seq(c, cat_seq):
  "category x category sequence -> truth value"
  return c in cat_seq
  
# ----- Datatypen lexicon entry -----

# Datatypen lexicon entry representerar en rad i ett lexikon. Ett sÃ¥dant entry
# Ã¤r en tupel bestÃ¥ende av ett ord (vÃ¤nstersidan) och en kategorisekvens
# (hÃ¶gersidan). Ett lexicon entry (fÃ¶rkortat lex_ent) lagras som en lista.

def create_lex_ent(word, categories):
  "word x category sequence -> lexicon entry"
  return [word, categories]
  
def word(lex_desc):
  "lexicon entry -> word"
  return lex_desc[0]
  
def categories(lex_desc):
  "lexicon entry -> category sequence"
  return lex_desc[1]
  
# ----- Datatypen lexicon -----

# Datatypen lexicon representerar ett lexikon, dvs en lista av ord med
# tillhÃ¶rande kategorier. Ett lexikon lagras som en lista dÃ¤r varje element
# Ã¤r av typen lexion entry (lex_ent).

def create_lexicon():
  "-> lexicon"
  return []

def is_empty_lexion(lex):
  "lexicon -> truth value"
  return not lex
  
def add_lex_ent(ent, lex):
  "lexicon x lexicon entry -> lexicon"
  return [ent] + lex

def first_entry(lex):
  "lexicon -> lex_ent"
  return lex[0]
  
def rest_lexicon(lex):
  "lexicon -> lexicon"
  return lex[1:]
  
def find_categories(w, lexicon):
  "word x lexicon -> category sequence"
  return categories(find_entry(w, lexicon, word))

def find_words(cat, lexicon):
  "category x lexicon -> lexicon"
  return extract_lexicon(lexicon, (lambda e: category_in_cat_seq(cat, categories(e))))

def extract_lexicon(lex, fn):
  "lexicon x (lex_ent -> truth value) -> table"
  if is_empty_lexion(lex):
    return create_lexicon()
  elif fn(first_entry(lex)):
    return add_lex_ent(first_entry(lex), extract_lexicon(rest_lexicon(lex), fn))
  else:
    return extract_lexicon(rest_lexicon(lex), fn)
  
# ----- Datatypen rule -----

# Datatypen rule representerar en grammatisk regel. Den Ã¤r en tupel bestÃ¥ende av
# en vÃ¤nstersida som Ã¤r en kategori och en hÃ¶gersida som Ã¤r en kategorisekvens.
# Regeln lagras som en lista.

def create_rule(lhs, rhs):
  "category x category sequence -> rule"
  return [lhs, rhs]
  
def rule_lhs(rule):
  "rule -> category"
  return rule[0]
  
def rule_rhs(rule):
  "rule -> category sequence"
  return rule[1]
  
# ----- Datatypen grammar -----

# Datatypen grammar representerar en grammatik, dvs en sekvens av regler. Den lagras
# som en lista.

def create_grammar():
  "-> grammar"
  return []
  
def add_rule(rule, grammar):
  "rule x grammar -> grammar"
  return [rule] + grammar
  
def is_empty_grammar(g):
  "grammar -> truth value"
  return not g

def first_rule(g):
  "grammar -> rule"
  return g[0]
   
def rest_grammar(g):
  "grammar -> grammar"
  return g[1:]
  
# *** Assignment A is to implement find_rules and extract_grammar ***

def find_rules(lhs, grammar):
  "category x grammar -> grammar"
  return "ASSIGNMENT A"
  
def is_terminalnode(cat, grammar):
  "category x grammar -> truth value"
  return is_empty_grammar(extract_grammar(grammar, (lambda rule: cat == rule_lhs(rule))))
  
def extract_grammar(grammar, fn):
  "grammar x (rule -> truth value) -> grammar"
  return "ASSIGNMENT A"

# ----- Extrafunktioner -----

import random

def random_element(tab):
  "grammar/lexicon -> entry"
  return tab[random.randint(0, len(tab)-1)]
 
def generate_sentence(cat, lex, gram):
  "category x lexicon x grammar -> sentence"
  return "ASSIGNMENT B"
      
# ----- Test -----
  
l = create_lexicon()
l = add_lex_ent(create_lex_ent('Karl', ['namn']), l)
l = add_lex_ent(create_lex_ent('Stina', ['namn']), l)
l = add_lex_ent(create_lex_ent('ser', ['verb']), l)
l = add_lex_ent(create_lex_ent('Ã¤ter', ['verb']), l)
l = add_lex_ent(create_lex_ent('en', ['artikel', 'substantiv']), l)
l = add_lex_ent(create_lex_ent('gris', ['substantiv']), l)
l = add_lex_ent(create_lex_ent('kung', ['substantiv']), l)

g = create_grammar()
g = add_rule(create_rule('mening', ['substantivfras', 'verbfras']), g)
g = add_rule(create_rule('verbfras', ['verb', 'substantivfras']), g)
g = add_rule(create_rule('substantivfras', ['namn']), g)
g = add_rule(create_rule('substantivfras', ['artikel', 'substantiv']), g)

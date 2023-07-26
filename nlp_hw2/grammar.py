# -*- coding: utf-8 -*-
"""grammar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W0VXdzFxUChZ-0w3nbXQI23N-LqxHjPt
"""

"""
COMS W4705 - Natural Language Processing - Summer 2022 
Homework 2 - Parsing with Context Free Grammars 
Daniel Bauer
"""

import sys
from collections import defaultdict
from math import fsum
import math

class Pcfg(object): 
    """
    Represent a probabilistic context free grammar. 
    """

    def __init__(self, grammar_file): 
        self.rhs_to_rules = defaultdict(list)
        self.lhs_to_rules = defaultdict(list)
        self.startsymbol = None 
        self.read_rules(grammar_file)      
 
    def read_rules(self,grammar_file):
        
        for line in grammar_file: 
            line = line.strip()
            if line and not line.startswith("#"):
                if "->" in line: 
                    rule = self.parse_rule(line.strip())
                    lhs, rhs, prob = rule
                    self.rhs_to_rules[rhs].append(rule)
                    self.lhs_to_rules[lhs].append(rule)
                else: 
                    startsymbol, prob = line.rsplit(";")
                    self.startsymbol = startsymbol.strip()
                    
     
    def parse_rule(self,rule_s):
        lhs, other = rule_s.split("->")
        lhs = lhs.strip()
        rhs_s, prob_s = other.rsplit(";",1) 
        prob = float(prob_s)
        rhs = tuple(rhs_s.strip().split())
        return (lhs, rhs, prob)

    def verify_grammar(self):
        """
        Return True if the grammar is a valid PCFG in CNF.
        Otherwise return False. 
        """
        #check if each rule is in chomsky normal form

        #create dictionary that keeps track of the sum of the probs for constant left hand sides
        lhs_prob_sums = dict()

        for lhs, rules in self.lhs_to_rules.items():
          for r in rules:

            if len(r) != 3:
              return False

            #check if rule is in CNF:
            rhs = r[1]
            if len(rhs) == 2:
              #A -> BC
              #check if nonterminals are uppercase
              for x in rhs:
                if x != x.upper():
                  return False
            elif len(rhs) == 1:
              # A -> b
              # check if terminal is lowercase
              if rhs[0] != rhs[0].lower():
                return False
            else:
              #not A -> BC or A -> b, thus not in CNF
              return False

            #sum probs with same lhs together in lhs_prob_sums dictionary:
            prob = r[2]
            lhs = r[0]

            if lhs in lhs_prob_sums:
              lhs_prob_sums[lhs] += prob
            else:
              lhs_prob_sums[lhs] = prob

        #check each lhs prob sum, if any are not close enough to one -> grammar is not a valid PCFG in CNF
        for lhs, prob in lhs_prob_sums.items():
          if not math.isclose(prob, 1.0):
            return False

        #at this point we have checked all the summed probilities and they are all close enough to 1:
        return True 


if __name__ == "__main__":
    with open("drive/MyDrive/hw2 3/atis3.pcfg",'r') as grammar_file:
        grammar = Pcfg(grammar_file)

    print(grammar.verify_grammar())
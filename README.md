# Parsing-with-CFG
Project for Natural Language Processing Course (COMS 4705) at Columbia University's School of Engineering and Applied Science, Oct 2022

In this project, I implemented the CKY algorithm for Context-Free Grammar and Probabilistic Context-Free Grammar parsing. I also practiced retrieving parse trees from a parse chart and working with such tree data structures. I worked with an existing PCFG grammar and a small test corpus. The main data for this project has been extracted from the ATIS (Air Travel Information Services) subsection of the Penn Treebank.

Python files:
- cky.py within nlp_hw2 contains my parser.
- grammar.py contains the class Pcfg which represents a PCFG grammar read in from a grammar file. 
- evaluate_parser.py contains a script that evaluates my parser against a test set.
Data files:
- atis3.pcfg - contains the PCFG grammar (980 rules)
- atis3_test.ptb - contains the test corpus (58 sentences).

Project Parts
1. Reading the grammar
2. Membership checking with CKY
3. Parsing with back pointers
4. Retrieving a parse tree
5. Evaluating the Parser



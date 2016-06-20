Tutorial
========
Once the package is installed, the user can import the package like this::

    import py_stringmatching as sm

The user begins by creating a tokenizer. **py_stringmatching** currently provides 5 different tokenizers - alphabetic tokenizer, alphanumeric tokenizer, delimiter based tokenizer, qgram tokenizer and whitespace tokenizer. A tokenizer can be created like this::

    # create a alphabetic tokenizer
    alphabet_tok = sm.AlphabeticTokenizer()
    
    # create a alphanumeric tokenizer
    alnum_tok = sm.AlphanumericTokenizer()
    
    # create a delimiter tokenizer using comma as a delimiter
    delim_tok = sm.DelimiterTokenizer(delim_set=[','])
    
    # create a qgram tokenizer using q=3
    qg_tok = sm.QgramTokenizer(qval=3)
    
    # create a whitespace tokenizer
    ws_tok = sm.WhitespaceTokenizer()

Next, the user needs to create a similarity measure object. **py_stringmatching** currently provides 14 different similarity measures. Few examples are shown below::

    # create a jaccard similarity measure object
    jac = sm.Jaccard()
    
    # create a levenshtein measure object
    lev = sm.Levenshtein()

Finally, the user can compute the similarity measure as follows::

    # input strings
    x = 'string matching package'
    y = 'string matching library'

    # compute jaccard measure over tokens of x and y, tokenized using whitespace
    jac_score = jac.get_raw_score(ws_tok.tokenize(x), ws_tok.tokenize(y))
    
    # compute levenshtein distance between x and y
    lev_dist = lev.get_raw_score(x, y)
    
Note that not all similarity measures are normalized between 0 and 1. For example, levenshtein distance can be greater than 1 wherer as measures like jaccard are always between 0 and 1. The user can obtain normalized similarity scores using the **get_sim_score** method::  

    # get normalized levenshtein similarity between x and y
    lev_norm_sim = lev.get_sim_score(x, y)
    
    # get normalized jaccard similarity (always equal to the raw score)
    jac_norm_sim = jac.get_sim_score(ws_tok.tokenize(x), ws_tok.tokenize(y))

Certain measures such as Affine Gap, Monge-Elkan, Needleman-Wunsch, Smith-Waterman and Soft-TFIDF do not have a **get_sim_score** method, as the raw score cannot be normalized for these similarity measures.  

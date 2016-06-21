"""Definition based tokenizer"""

from py_stringmatching.tokenizer.tokenizer import Tokenizer


class DefinitionTokenizer(Tokenizer):
    """Definition based tokenizer class.

    Parameters:
        return_set (boolean): flag to indicate whether to return a set of
                              tokens. (defaults to False)
        is_lowercase (boolean): flag to indicate whether to convert the input
                              to all lowercase. (defaults to False)
    """
    def __init__(self, return_set=False, is_lowercase=False):
        super(DefinitionTokenizer, self).__init__(return_set, is_lowercase)

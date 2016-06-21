"""Whitespace based tokenizer"""

from py_stringmatching import utils
from py_stringmatching.tokenizer.delimiter_tokenizer import DelimiterTokenizer


class WhitespaceTokenizer(DelimiterTokenizer):
    """Whitespace tokenizer class.

    Parameters:
        return_set (boolean): flag to indicate whether to return a set of
                              tokens. (defaults to False)
        is_lowercase (boolean): flag to indicate whether to convert the input
                              to all lowercase. (defaults to False)
    """
    def __init__(self, return_set=False, is_lowercase=False):
        super(WhitespaceTokenizer, self).__init__(set(), return_set, is_lowercase)

    def tokenize(self, input_string):
        """
        Tokenizes input string based on white space.

        Args:
            input_string (str): Input string

        Returns:
            Token list (list)

        Raises:
            TypeError : If the input is not a string

        Examples:
            >>> ws_tok = WhitespaceTokenizer() 
            >>> ws_tok.tokenize('data science')
            ['data', 'science']
            >>> ws_tok.tokenize('data        science')
            ['data', 'science']
            >>> ws_tok.tokenize('data\tscience')
            ['data', 'science']
            >>> ws_tok = WhitespaceTokenizer(return_set=True) 
            >>> ws_tok.tokenize('data   science data integration')
            ['data', 'science', 'integration']

        """
        utils.tok_check_for_none(input_string)
        utils.tok_check_for_string_input(input_string)

        if self.is_lowercase:
            input_string = input_string.lower()

        token_list =  list(filter(None, input_string.split()))

        if self.return_set:
            return utils.convert_bag_to_set(token_list)

        return token_list

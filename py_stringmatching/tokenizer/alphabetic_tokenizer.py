"""Alphabetic tokenizer"""

import re

from py_stringmatching import utils
from py_stringmatching.tokenizer.definition_tokenizer import DefinitionTokenizer


class AlphabeticTokenizer(DefinitionTokenizer):
    """Alphabetic tokenizer class.

    Parameters:
        return_set (boolean): flag to indicate whether to return a set of
                              tokens. (defaults to False)
        is_lowercase (boolean): flag to indicate whether to convert the input
                              to all lowercase. (defaults to False)
    """
    def __init__(self, return_set=False, is_lowercase=False):
        self.al_regex = re.compile('[a-zA-Z]+')
        super(AlphabeticTokenizer, self).__init__(return_set, is_lowercase)

    def tokenize(self, input_string):
        """
        Tokenizes input string into alphabetic tokens.

        An alphabetic token is defined as consecutive sequence of alphabetic characters.

        Args:
            input_string (str): Input string

        Returns:
            Token list (list)

        Raises:
            TypeError : If the input is not a string

        Examples:
            >>> al_tok = AlphabeticTokenizer()
            >>> al_tok.tokenize('data99science, data#integration.')
            ['data', 'science', 'data', 'integration']
            >>> al_tok.tokenize('99')
            []
            >>> al_tok = AlphabeticTokenizer(return_set=True) 
            >>> al_tok.tokenize('data99science, data#integration.')
            ['data', 'science', 'integration']
                      
        """
        utils.tok_check_for_none(input_string)
        utils.tok_check_for_string_input(input_string)

        if self.is_lowercase:
            input_string = input_string.lower()

        token_list = list(filter(None, self.al_regex.findall(input_string)))

        if self.return_set:
            return utils.convert_bag_to_set(token_list)

        return token_list

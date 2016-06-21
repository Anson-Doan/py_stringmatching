"""Delimiter based tokenizer"""

import re

from py_stringmatching import utils
from py_stringmatching.tokenizer.tokenizer import Tokenizer


class DelimiterTokenizer(Tokenizer):
    """Delimiter tokenizer class.

    Parameters:
        delim_set (set): set of delimiter strings (defaults to space delimiter)
        return_set (boolean): flag to indicate whether to return a set of
                              tokens. (defaults to False)
        is_lowercase (boolean): flag to indicate whether to convert the input
                              to all lowercase. (defaults to False)
    """
    def __init__(self, delim_set=set([' ']), return_set=False, is_lowercase=False):
        self.__delim_set = None
        self.__use_split = None
        self.__delim_str = None
        self.__delim_regex = None
        self.set_delim_set(delim_set)
        super(DelimiterTokenizer, self).__init__(return_set, is_lowercase)

    def tokenize(self, input_string):
        """
        Tokenizes input string based on the set of delimiters.

        Args:
            input_string (str): Input string

        Returns:
            Token list (list)

        Raises:
            TypeError : If the input is not a string

        Examples:
            >>> delim_tok = DelimiterTokenizer() 
            >>> delim_tok.tokenize('data science')
            ['data', 'science']
            >>> delim_tok = DelimiterTokenizer(['$#$']) 
            >>> delim_tok.tokenize('data$#$science')
            ['data', 'science']
            >>> delim_tok = DelimiterTokenizer([',', '.']) 
            >>> delim_tok.tokenize('data,science.data,integration.')
            ['data', 'science', 'data', 'integration']
            >>> delim_tok = DelimiterTokenizer([',', '.'], return_set=True) 
            >>> delim_tok.tokenize('data,science.data,integration.')
            ['data', 'science', 'integration']

        """
        utils.tok_check_for_none(input_string)
        utils.tok_check_for_string_input(input_string)

        if self.is_lowercase:
            input_string = input_string.lower()
    
        if self.__use_split:
            token_list = list(filter(None,
                                     input_string.split(self.__delim_str)))
        else:
            token_list = list(filter(None,
                                     self.__delim_regex.split(input_string)))

        if self.return_set:
            return utils.convert_bag_to_set(token_list)

        return token_list

    def get_delim_set(self):
        """
        Get the current set of delimiters
        
        Returns:
            Delimiter set (set)
        """
        return self.__delim_set

    def set_delim_set(self, delim_set):
        """
        Set delimiters
        
        Args:
            delim_set (set): set of delimiter strings 
        """
        if not isinstance(delim_set, set):
            delim_set = set(delim_set)
        self.__delim_set = delim_set
        # if there is only one delimiter string, use split instead of regex
        self.__use_split = False
        if len(self.__delim_set) == 1:
            self.__delim_str = list(self.__delim_set)[0]
            self.__use_split = True
        else:
            self.__delim_regex = re.compile('|'.join(
                                     map(re.escape, self.__delim_set)))
        return True    

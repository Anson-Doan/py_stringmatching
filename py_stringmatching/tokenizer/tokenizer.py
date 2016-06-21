"""Tokenizer"""

class Tokenizer(object):
    """Tokenizer class.

    Parameters:
        return_set (boolean): an attribute which is a flag to indicate whether to return a set of
                              tokens instead of a bag of tokens (defaults to False).
        is_lowercase (boolean): an attribute which is a flag to indicate whether to convert the input
                              entirely into lowercase (defaults to False).
    """
    def __init__(self, return_set=False, is_lowercase=False):
        self.return_set = return_set
        self.is_lowercase = is_lowercase

    def get_return_set(self):
        """Get the return_set flag.

        Returns:
            The boolean value of the return_set attribute.
        """
        return self.return_set

    def set_return_set(self, return_set):
        """Set the return_set flag.

        Args:
            return_set (boolean): flag to indicate whether to return a set of tokens or a bag of tokens. 
        """
        self.return_set = return_set
        return True

    def get_is_lowercase(self):
        """Get the is_lowercase flag.

        Returns:
            The boolean value of the is_lowercase attribute.
        """
        return self.is_lowercase

    def set_is_lowercase(self, is_lowercase):
        """Set the is_lowercase flag.

        Args:
            is_lowercase (boolean): flag to indicate whether to convert input to all lowercase.
        """
        self.is_lowercase = is_lowercase
        return True

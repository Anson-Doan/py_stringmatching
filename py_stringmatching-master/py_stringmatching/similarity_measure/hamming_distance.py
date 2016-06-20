"""Hamming distance measure"""

from __future__ import division

from py_stringmatching import utils
from py_stringmatching.similarity_measure.sequence_similarity_measure import \
                                                    SequenceSimilarityMeasure


class HammingDistance(SequenceSimilarityMeasure):
    """Hamming distance measure class.
    """
    def __init__(self):
        super(HammingDistance, self).__init__()

    def get_raw_score(self, string1, string2):
        """
        Computes the Hamming distance between two strings.

        The Hamming distance between two strings of equal length is the number of positions at which the corresponding
        symbols are different. In another way, it measures the minimum number of substitutions required to change
        one string into the other, or the minimum number of errors that could have transformed one string into the other.

        Args:
            string1,string2 (str): Input strings

        Returns:
            Hamming distance (int)

        Raises:
            TypeError : If the inputs are not strings or if one of the inputs is None.
            ValueError : If the input strings are not of same length

        Examples:
            >>> hd = HammingDistance()
            >>> hd.get_raw_score('', '')
            0
            >>> hd.get_raw_score('alex', 'john')
            4
            >>> hd.get_raw_score(' ', 'a')
            1
            >>> hd.get_raw_score('JOHN', 'john')
            4
        """
        # input validations
        utils.sim_check_for_none(string1, string2)
        utils.tok_check_for_string_input(string1, string2)

        # for Hamming Distance string length should be same
        utils.sim_check_for_same_len(string1, string2)

        # sum all the mismatch characters at the corresponding index of
        # input strings
        return sum(bool(ord(c1) - ord(c2)) for c1, c2 in zip(string1, string2))

    def get_sim_score(self, string1, string2):
        """
        Computes the normalized hamming similarity between two strings.

        Args:
            string1,string2 (str): Input strings

        Returns:
            Normalized hamming similarity (float)

        Raises:
            TypeError : If the inputs are not strings or if one of the inputs is None.
            ValueError : If the input strings are not of same length

        Examples:
            >>> hd = HammingDistance()
            >>> hd.get_sim_score('', '')
            1.0
            >>> hd.get_sim_score('alex', 'john')
            0.0
            >>> hd.get_sim_score(' ', 'a')
            0.0
            >>> hd.get_sim_score('JOHN', 'john')
            0.0
        """
        raw_score = self.get_raw_score(string1, string2)
        common_len = len(string1)
        if common_len == 0:
            return 1.0
        return 1 - (raw_score / common_len)

"""Levenshtein distance measure"""

from __future__ import division

from py_stringmatching import utils
from py_stringmatching.similarity_measure.cython_levenshtein import levenshtein
from py_stringmatching.similarity_measure.sequence_similarity_measure import \
                                                    SequenceSimilarityMeasure


class Levenshtein(SequenceSimilarityMeasure):
    """Levenshtein distance measure class.
    """
    def __init__(self):
        super(Levenshtein, self).__init__()

    def get_raw_score(self, string1, string2):
        """
        Computes the Levenshtein distance between two strings.

        Levenshtein distance computes the minimum cost of transforming one string into the other. Transforming a string
        is carried out using a sequence of the following operators: delete a character, insert a character, and
        substitute one character for another.

        Args:
            string1,string2 (str): Input strings

        Returns:
            Levenshtein distance (int)

        Raises:
            TypeError : If the inputs are not strings

        Examples:
            >>> lev = Levenshtein()
            >>> lev.get_raw_score('a', '')
            1
            >>> lev.get_raw_score('example', 'samples')
            3
            >>> lev.get_raw_score('levenshtein', 'frankenstein')
            6

        """
        # input validations
        utils.sim_check_for_none(string1, string2)
        utils.sim_check_for_string_inputs(string1, string2)
        if utils.sim_check_for_exact_match(string1, string2):
            return 0.0
        return levenshtein(string1, string2)

    def get_sim_score(self, string1, string2):
        """
        Computes the normalized levenshtein similarity between two strings.

        Args:
            string1,string2 (str): Input strings

        Returns:
            Normalized levenshtein similarity (float)

        Raises:
            TypeError : If the inputs are not strings

        Examples:
            >>> lev = Levenshtein()
            >>> lev.get_sim_score('a', '')
            0.0
            >>> lev.get_sim_score('example', 'samples')
            0.5714285714285714
            >>> lev.get_sim_score('levenshtein', 'frankenstein')
            0.5

        """
        raw_score = self.get_raw_score(string1, string2)
        max_len = max(len(string1), len(string2))
        if max_len == 0:
            return 1.0
        return 1 - (raw_score / max_len)

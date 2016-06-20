# coding=utf-8
"""Smith-Waterman measure"""

import numpy as np

from py_stringmatching import utils
from six.moves import xrange
from py_stringmatching.similarity_measure.sequence_similarity_measure import \
                                                    SequenceSimilarityMeasure


def sim_ident(char1, char2):
    return int(char1 == char2)


class SmithWaterman(SequenceSimilarityMeasure):
    """Smith-Waterman similarity measure class.

    Parameters:
        gap_cost (float): Cost of gap (defaults to 1.0)
        sim_func (function): Similarity function to give a score for the correspondence between characters. Defaults
                              to an identity function, where if two characters are same it returns 1 else returns 0.
    """
    def __init__(self, gap_cost=1.0, sim_func=sim_ident):
        self.gap_cost = gap_cost
        self.sim_func = sim_func
        super(SmithWaterman, self).__init__()

    def get_raw_score(self, string1, string2):
        """
        Computes the Smith-Waterman measure between two strings.

        The Smith-Waterman algorithm performs local sequence alignment; that is, for determining similar regions
        between two strings. Instead of looking at the total sequence, the Smith–Waterman algorithm compares segments of
        all possible lengths and optimizes the similarity measure.


        Args:
            string1,string2 (str) : Input strings

        Returns:
            Smith-Waterman measure (float)

        Raises:
            TypeError : If the inputs are not strings or if one of the inputs is None.

        Examples:
            >>> sw = SmithWaterman()
            >>> sw.get_raw_score('cat', 'hat')
            2.0
            >>> sw = SmithWaterman(gap_cost=2.2)
            >>> sw.get_raw_score('dva', 'deeve')
            1.0
            >>> sw = SmithWaterman(gap_cost=1, sim_func=lambda s1, s2 : (2 if s1 == s2 else -1))
            >>> sw.get_raw_score('dva', 'deeve')
            2.0
            >>> sw = SmithWaterman(gap_cost=1.4, sim_func=lambda s1, s2 : (1.5 if s1 == s2 else 0.5))
            >>> sw.get_raw_score('GCATAGCU', 'GATTACA')
            6.5
        """
        # input validations
        utils.sim_check_for_none(string1, string2)
        utils.sim_check_for_string_inputs(string1, string2)

        dist_mat = np.zeros((len(string1) + 1, len(string2) + 1),
                            dtype=np.float)
        max_value = 0
        # Smith Waterman DP calculations
        for i in xrange(1, len(string1) + 1):
            for j in xrange(1, len(string2) + 1):
                match = dist_mat[i - 1, j - 1] + self.sim_func(string1[i - 1],
                                                               string2[j - 1])
                delete = dist_mat[i - 1, j] - self.gap_cost
                insert = dist_mat[i, j - 1] - self.gap_cost
                dist_mat[i, j] = max(0, match, delete, insert)
                max_value = max(max_value, dist_mat[i, j])

        return max_value

    def get_gap_cost(self):
        """
        Get gap cost

        Returns:
            gap cost (float)
        """
        return self.gap_cost

    def get_sim_func(self):
        """
        Get similarity function

        Returns:
            similarity function (function)
        """
        return self.sim_func

    def set_gap_cost(self, gap_cost):
        """
        Set gap cost

        Args:
            gap_cost (float): Cost of gap
        """
        self.gap_cost = gap_cost
        return True

    def set_sim_func(self, sim_func):
        """
        Set similarity function

        Args:
            sim_func (function): Similarity function to give a score for the correspondence between characters.
        """
        self.sim_func = sim_func
        return True

"""Jaro-Winkler similarity measure"""

from py_stringmatching import utils
from py_stringmatching.similarity_measure.jaro import Jaro
from py_stringmatching.similarity_measure.sequence_similarity_measure import \
                                                    SequenceSimilarityMeasure


class JaroWinkler(SequenceSimilarityMeasure):
    """Jaro-Winkler similarity measure class.

    Parameters:
        prefix_weight (float): Weight to give the prefix (defaults to 0.1)
    """
    def __init__(self, prefix_weight=0.1):
        self.prefix_weight = prefix_weight
        super(JaroWinkler, self).__init__()

    def get_raw_score(self, string1, string2):
        """
        Computes the Jaro-Winkler measure between two strings.

        The Jaro-Winkler measure is designed to capture cases where two strings have a low Jaro score, but share a prefix
        and thus are likely to match.

        Args:
            string1,string2 (str): Input strings

        Returns:
            Jaro-Winkler measure (float)

        Raises:
            TypeError : If the inputs are not strings or if one of the inputs is None.

        Examples:
            >>> jw = JaroWinkler()
            >>> jw.get_raw_score('MARTHA', 'MARHTA')
            0.9611111111111111
            >>> jw.get_raw_score('DWAYNE', 'DUANE')
            0.84
            >>> jw.get_raw_score('DIXON', 'DICKSONX')
            0.8133333333333332

        """
        # input validations
        utils.sim_check_for_none(string1, string2)
        utils.tok_check_for_string_input(string1, string2)

        # if one of the strings is empty return 0
        if utils.sim_check_for_empty(string1, string2):
            return 0

        jw_score = Jaro().get_raw_score(string1, string2)
        min_len = min(len(string1), len(string2))

        # prefix length can be at max 4
        j = min(min_len, 4)
        i = 0
        while i < j and string1[i] == string2[i] and string1[i]:
            i += 1

        if i:
            jw_score += i * self.prefix_weight * (1 - jw_score)

        return jw_score

    def get_sim_score(self, string1, string2):
        """
        Computes the normalized jaro-winkler similarity between two strings.

        Args:
            string1,string2 (str): Input strings

        Returns:
            Normalized jaro-winkler similarity (float)

        Raises:
            TypeError : If the inputs are not strings or if one of the inputs is None.

        Examples:
            >>> jw = JaroWinkler()
            >>> jw.get_sim_score('MARTHA', 'MARHTA')
            0.9611111111111111
            >>> jw.get_sim_score('DWAYNE', 'DUANE')
            0.84
            >>> jw.get_sim_score('DIXON', 'DICKSONX')
            0.8133333333333332

        """
        return self.get_raw_score(string1, string2)

    def get_prefix_weight(self):
        """
        Get prefix weight

        Returns:
            prefix weight (float)
        """
        return self.prefix_weight

    def set_prefix_weight(self, prefix_weight):
        """
        Set prefix weight

        Args:
            prefix_weight (float): Weight to give the prefix
        """
        self.prefix_weight = prefix_weight
        return True

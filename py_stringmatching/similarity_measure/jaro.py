"""Jaro similarity measure"""

from py_stringmatching import utils
from py_stringmatching.compat import _range
from py_stringmatching.similarity_measure.sequence_similarity_measure import \
                                                    SequenceSimilarityMeasure


class Jaro(SequenceSimilarityMeasure):
    def __init__(self):
        super(Jaro, self).__init__()

    def get_raw_score(self, string1, string2):
        """
        Computes the jaro measure between two strings.

        The Jaro measure is a type of edit distance, This was developed mainly to compare short strings,
        such as first and last names.

        Args:
            string1,string2 (str): Input strings

        Returns:
            Jaro measure (float)

        Raises:
            TypeError : If the inputs are not strings or if one of the inputs is None.

        Examples:
            >>> jaro = Jaro()
            >>> jaro.get_raw_score('MARTHA', 'MARHTA')
            0.9444444444444445
            >>> jaro.get_raw_score('DWAYNE', 'DUANE')
            0.8222222222222223
            >>> jaro.get_raw_score('DIXON', 'DICKSONX')
            0.7666666666666666

        """
        # input validations
        utils.sim_check_for_none(string1, string2)
        utils.tok_check_for_string_input(string1, string2)

        # if one of the strings is empty return 0
        if utils.sim_check_for_empty(string1, string2):
            return 0

        len_s1 = len(string1)
        len_s2 = len(string2)

        max_len = max(len_s1, len_s2)
        search_range = (max_len // 2) - 1
        if search_range < 0:
            search_range = 0

        flags_s1 = [False] * len_s1
        flags_s2 = [False] * len_s2

        common_chars = 0
        for i, ch_s1 in enumerate(string1):
            low = i - search_range if i > search_range else 0
            hi = i + search_range if i + search_range < len_s2 else len_s2 - 1
            for j in _range(low, hi + 1):
                if not flags_s2[j] and string2[j] == ch_s1:
                    flags_s1[i] = flags_s2[j] = True
                    common_chars += 1
                    break

        if not common_chars:
            return 0

        k = trans_count = 0
        for i, f_s1 in enumerate(flags_s1):
            if f_s1:
                for j in _range(k, len_s2):
                    if flags_s2[j]:
                        k = j + 1
                        break
                if string1[i] != string2[j]:
                    trans_count += 1

        trans_count /= 2
        common_chars = float(common_chars)
        weight = ((common_chars / len_s1 + common_chars / len_s2 +
                   (common_chars - trans_count) / common_chars)) / 3
        return weight

    def get_sim_score(self, string1, string2):
        """
        Computes the normalized jaro similarity between two strings.

        Args:
            string1,string2 (str): Input strings

        Returns:
            Normalized jaro similarity (float)

        Raises:
            TypeError : If the inputs are not strings or if one of the inputs is None.

        Examples:
            >>> jaro = Jaro()
            >>> jaro.get_sim_score('MARTHA', 'MARHTA')
            0.9444444444444445

        """
        return self.get_raw_score(string1, string2)

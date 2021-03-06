"""Dice similarity measure"""

from py_stringmatching import utils
from py_stringmatching.similarity_measure.token_similarity_measure import \
                                                    TokenSimilarityMeasure


class Dice(TokenSimilarityMeasure):
    """Dice similarity measure class.
    """
    def __init__(self):
        super(Dice, self).__init__()

    def get_raw_score(self, set1, set2):
        """
        Computes the dice similarity coefficient between two sets.

        The similarity is defined as twice the shared information (intersection) divided by sum of cardinalities.
        For two sets X and Y, the Dice similarity coefficient is:

        :math:`dice(X, Y) = \\frac{2 * |X \\cap Y|}{|X| + |Y|}`

        Args:
            set1,set2 (set or list): Input sets (or lists). Input lists are converted to sets.

        Returns:
            Dice similarity coefficient (float)

        Raises:
            TypeError : If the inputs are not sets (or lists) or if one of the inputs is None.

        Examples:
            >>> dice = Dice()
            >>> dice.get_raw_score(['data', 'science'], ['data'])
            0.6666666666666666
            >>> dice.get_raw_score({1, 1, 2, 3, 4}, {2, 3, 4, 5, 6, 7, 7, 8})
            0.5454545454545454
            >>> dice.get_raw_score(['data', 'management'], ['data', 'data', 'science'])
            0.5

        References:
            * Wikipedia article : https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Dice%27s_coefficient
            * Simmetrics library
        """
        # input validations
        utils.sim_check_for_none(set1, set2)
        utils.sim_check_for_list_or_set_inputs(set1, set2)

        # if exact match return 1.0
        if utils.sim_check_for_exact_match(set1, set2):
            return 1.0

        # if one of the strings is empty return 0
        if utils.sim_check_for_empty(set1, set2):
            return 0

        if not isinstance(set1, set):
            set1 = set(set1)
        if not isinstance(set2, set):
            set2 = set(set2)

        return 2.0 * float(len(set1 & set2)) / float(len(set1) + len(set2))

    def get_sim_score(self, set1, set2):
        """
        Computes the normalized dice similarity between two sets.

        Args:
            set1,set2 (set or list): Input sets (or lists). Input lists are converted to sets.

        Returns:
            Normalized dice similarity (float)

        Raises:
            TypeError : If the inputs are not sets (or lists) or if one of the inputs is None.

        Examples:
            >>> dice = Dice()
            >>> dice.get_sim_score(['data', 'science'], ['data'])
            0.6666666666666666
            >>> dice.get_sim_score({1, 1, 2, 3, 4}, {2, 3, 4, 5, 6, 7, 7, 8})
            0.5454545454545454
            >>> dice.get_sim_score(['data', 'management'], ['data', 'data', 'science'])
            0.5

        """
        return self.get_raw_score(set1, set2)

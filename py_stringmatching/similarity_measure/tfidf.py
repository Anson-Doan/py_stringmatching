"""Tf-Idf similarity measure"""

from __future__ import division
from math import log, sqrt
import collections

from py_stringmatching import utils
from py_stringmatching.similarity_measure.token_similarity_measure import \
                                                    TokenSimilarityMeasure


class TfIdf(TokenSimilarityMeasure):
    """Tf-Idf similarity measure class.

    Parameters:
        corpus_list (list of lists): Corpus list (default is set to None) of strings. If set to None,
                                     the input list are considered the only corpus.
        dampen (boolean): Flag to indicate whether 'log' should be applied to tf and idf measure.
    """
    def __init__(self, corpus_list=None, dampen=False):
        self.__corpus_list = corpus_list
        self.__document_frequency = {}
        self.__compute_document_frequency()
        self.__corpus_size = 0 if self.__corpus_list is None else (
                                                         len(self.__corpus_list))
        self.dampen = dampen        
        super(TfIdf, self).__init__()

    def get_raw_score(self, bag1, bag2):
        """
        Compute TF-IDF measure between two lists given the corpus information.

        This measure employs the notion of TF/IDF score commonly used in information retrieval (IR) to
        find documents that are relevant to keyword queries. The intuition underlying the TF/IDF measure
        is that two strings are similar if they share distinguishing terms.

        Args:
            bag1,bag2 (list): Input lists

        Returns:
            TF-IDF measure between the input lists (float)

        Raises:
            TypeError : If the inputs are not lists or if one of the inputs is None

        Examples:
            
            >>> tfidf = TfIdf([['a', 'b', 'a'], ['a', 'c'], ['a']])
            >>> tfidf.get_raw_score(['a', 'b', 'a'], ['a', 'c'])
            0.17541160386140586
            >>> tfidf.get_raw_score(['a', 'b', 'a'], ['a'])
            0.5547001962252291
            >>> tfidf = TfIdf([['a', 'b', 'a'], ['a', 'c'], ['a'], ['b']], True)
            >>> tfidf.get_raw_score(['a', 'b', 'a'], ['a', 'c'])
            0.11166746710505392
            >>> tfidf = TfIdf([['x', 'y'], ['w'], ['q']])
            >>> tfidf.get_raw_score(['a', 'b', 'a'], ['a'])
            0.0
            >>> tfidf = TfIdf([['x', 'y'], ['w'], ['q']], True)
            >>> tfidf.get_raw_score(['a', 'b', 'a'], ['a'])
            0.0
            >>> tfidf = TfIdf()
            >>> tfidf.get_raw_score(['a', 'b', 'a'], ['a'])
            0.7071067811865475
        """
        # input validations
        utils.sim_check_for_none(bag1, bag2)
        utils.sim_check_for_list_or_set_inputs(bag1, bag2)

        # if the strings match exactly return 1.0
        if utils.sim_check_for_exact_match(bag1, bag2):
            return 1.0

        # if one of the strings is empty return 0
        if utils.sim_check_for_empty(bag1, bag2):
            return 0

        # term frequency for input strings
        tf_x, tf_y = collections.Counter(bag1), collections.Counter(bag2)
         
        # find unique elements in the input lists and their document frequency 
        local_df = {}
        for element in tf_x:
            local_df[element] = local_df.get(element, 0) + 1
        for element in tf_y:
            local_df[element] = local_df.get(element, 0) + 1

        # if corpus is not provided treat input string as corpus
        curr_df, corpus_size = (local_df, 2) if self.__corpus_list is None else (
                                   (self.__document_frequency, self.__corpus_size))

        idf_element, v_x, v_y, v_x_y, v_x_2, v_y_2 = (0.0, 0.0, 0.0, 
                                                      0.0, 0.0, 0.0)

        # tfidf calculation
        for element in local_df.keys():
            df_element = curr_df.get(element)
            if df_element is None:
                continue
            idf_element = corpus_size * 1.0 / df_element
            v_x = 0 if element not in tf_x else (log(idf_element) * log(tf_x[element] + 1)) if self.dampen else (
                  idf_element * tf_x[element])
            v_y = 0 if element not in tf_y else (log(idf_element) * log(tf_y[element] + 1)) if self.dampen else (
                  idf_element * tf_y[element])
            v_x_y += v_x * v_y
            v_x_2 += v_x * v_x
            v_y_2 += v_y * v_y

        return 0.0 if v_x_y == 0 else v_x_y / (sqrt(v_x_2) * sqrt(v_y_2))

    def get_sim_score(self, bag1, bag2):
        """
        Compute normalized TF-IDF similarity between two lists given the corpus information.

        This measure employs the notion of TF/IDF score commonly used in information retrieval (IR) to
        find documents that are relevant to keyword queries. The intuition underlying the TF/IDF measure
        is that two strings are similar if they share distinguishing terms.

        Args:
            bag1,bag2 (list): Input lists

        Returns:
            Normalized TF-IDF similarity between the input lists (float)

        Raises:
            TypeError : If the inputs are not lists or if one of the inputs is None

        Examples:
            
            >>> tfidf = TfIdf([['a', 'b', 'a'], ['a', 'c'], ['a']])
            >>> tfidf.get_sim_score(['a', 'b', 'a'], ['a', 'c'])
            0.17541160386140586
            >>> tfidf.get_sim_score(['a', 'b', 'a'], ['a'])
            0.5547001962252291
            >>> tfidf = TfIdf([['a', 'b', 'a'], ['a', 'c'], ['a'], ['b']], True)
            >>> tfidf.get_sim_score(['a', 'b', 'a'], ['a', 'c'])
            0.11166746710505392
            >>> tfidf = TfIdf([['x', 'y'], ['w'], ['q']])
            >>> tfidf.get_sim_score(['a', 'b', 'a'], ['a'])
            0.0
            >>> tfidf = TfIdf([['x', 'y'], ['w'], ['q']], True)
            >>> tfidf.get_sim_score(['a', 'b', 'a'], ['a'])
            0.0
            >>> tfidf = TfIdf()
            >>> tfidf.get_sim_score(['a', 'b', 'a'], ['a'])
            0.7071067811865475
        """
        return self.get_raw_score(bag1, bag2)

    def get_dampen(self):
        """
        Get dampen flag

        Returns:
            dampen flag (boolean)
        """
        return self.dampen

    def get_corpus_list(self):
        """
        Get corpus list

        Returns:
            corpus list (list of lists)
        """
        return self.__corpus_list

    def set_dampen(self, dampen):
        """
        Set dampen flag

        Args:
            dampen (boolean): Flag to indicate whether 'log' should be applied to tf and idf measure.
        """
        self.dampen = dampen
        return True

    def set_corpus_list(self, corpus_list):
        """
        Set corpus list

        Args:
            corpus_list (list of lists): Corpus list
        """
        self.__corpus_list = corpus_list
        self.__document_frequency = {}
        self.__compute_document_frequency()
        self.__corpus_size = 0 if self.__corpus_list is None else (
                                                         len(self.__corpus_list))
        return True

    def __compute_document_frequency(self):
        if self.__corpus_list != None:
            for document in self.__corpus_list:
                for element in set(document):
                    self.__document_frequency[element] = ( 
                        self.__document_frequency.get(element, 0) + 1)

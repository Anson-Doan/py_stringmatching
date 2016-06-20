# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

# sequence based similarity measures
from py_stringmatching.similarity_measure.affine import Affine
from py_stringmatching.similarity_measure.bag_distance import BagDistance
from py_stringmatching.similarity_measure.editex import Editex
from py_stringmatching.similarity_measure.hamming_distance import HammingDistance
from py_stringmatching.similarity_measure.jaro import Jaro
from py_stringmatching.similarity_measure.jaro_winkler import JaroWinkler
from py_stringmatching.similarity_measure.levenshtein import Levenshtein
from py_stringmatching.similarity_measure.needleman_wunsch import NeedlemanWunsch
from py_stringmatching.similarity_measure.smith_waterman import SmithWaterman
# token based similarity measures
from py_stringmatching.similarity_measure.cosine import Cosine
from py_stringmatching.similarity_measure.dice import Dice
from py_stringmatching.similarity_measure.jaccard import Jaccard
from py_stringmatching.similarity_measure.overlap_coefficient import OverlapCoefficient
from py_stringmatching.similarity_measure.soft_tfidf import SoftTfIdf
from py_stringmatching.similarity_measure.tfidf import TfIdf
from py_stringmatching.similarity_measure.tversky_index import TverskyIndex
# hybrid similarity measures
from py_stringmatching.similarity_measure.generalized_jaccard import GeneralizedJaccard
from py_stringmatching.similarity_measure.monge_elkan import MongeElkan
#phonetic similarity measures
from py_stringmatching.similarity_measure.soundex import Soundex

from . import _short_string_1, _long_string_1, _medium_string_1, _short_string_2, _long_string_2, _medium_string_2
from . import _small_num_tokens_wi_rep, _small_num_tokens_wo_rep, _med_num_tokens_wi_rep, _med_num_tokens_wo_rep, \
    _large_num_tokens_wi_rep, _large_num_tokens_wo_rep, _long_hamm_string1, _long_hamm_string2


class TimeAffine:
    def setup(self):
        self.affine = Affine()

    def time_short_short(self):
        self.affine.get_raw_score(_short_string_1, _short_string_2)

    def time_medium_medium(self):
        self.affine.get_raw_score(_medium_string_1, _medium_string_2)

    def time_long_long(self):
        self.affine.get_raw_score(_long_string_1, _long_string_2)

    def time_short_medium(self):
        self.affine.get_raw_score(_short_string_1, _medium_string_1)

    def time_short_long(self):
        self.affine.get_raw_score(_short_string_1, _long_string_1)

    def time_medium_long(self):
        self.affine.get_raw_score(_medium_string_1, _long_string_1)


class TimeJaro:
    def setup(self):
        self.jaro = Jaro()

    def time_short_short(self):
        self.jaro.get_raw_score(_short_string_1, _short_string_2)

    def time_medium_medium(self):
        self.jaro.get_raw_score(_medium_string_1, _medium_string_2)

    def time_long_long(self):
        self.jaro.get_raw_score(_long_string_1, _long_string_2)

    def time_short_medium(self):
        self.jaro.get_raw_score(_short_string_1, _medium_string_1)

    def time_short_long(self):
        self.jaro.get_raw_score(_short_string_1, _long_string_1)

    def time_medium_long(self):
        self.jaro.get_raw_score(_medium_string_1, _long_string_1)


class TimeJaroWinkler:
    def setup(self):
        self.jaro_winkler = JaroWinkler()

    def time_short_short(self):
        self.jaro_winkler.get_raw_score(_short_string_1, _short_string_2)

    def time_medium_medium(self):
        self.jaro_winkler.get_raw_score(_medium_string_1, _medium_string_2)

    def time_long_long(self):
        self.jaro_winkler.get_raw_score(_long_string_1, _long_string_2)

    def time_short_medium(self):
        self.jaro_winkler.get_raw_score(_short_string_1, _medium_string_1)

    def time_short_long(self):
        self.jaro_winkler.get_raw_score(_short_string_1, _long_string_1)

    def time_medium_long(self):
        self.jaro_winkler.get_raw_score(_medium_string_1, _long_string_1)


class TimeHammingDistance:
    def setup(self):
        self.hamming_distance = HammingDistance()

    def time_short_short(self):
        self.hamming_distance.get_raw_score(_short_string_1, _short_string_1)

    def time_medium_medium(self):
        self.hamming_distance.get_raw_score(_medium_string_1, _medium_string_1)

    def time_long_long(self):
        self.hamming_distance.get_raw_score(_long_hamm_string1, _long_hamm_string2)

        # def time_short_medium(self):
        #     self.hamming_distance.get_raw_score(_short_string_1, _medium_string_1)
        #
        # def time_short_long(self):
        #     self.hamming_distance.get_raw_score(_short_string_1, _long_string_1)
        #
        # def time_medium_long(self):
        #     self.hamming_distance.get_raw_score(_medium_string_1, _long_string_1)


class TimeEditex:
    def setup(self):
        self.editex = Editex()

    def time_short_short(self):
        self.editex.get_raw_score(_short_string_1, _short_string_2)

    def time_medium_medium(self):
        self.editex.get_raw_score(_medium_string_1, _medium_string_2)

    def time_long_long(self):
        self.editex.get_raw_score(_long_string_1, _long_string_2)

    def time_short_medium(self):
        self.editex.get_raw_score(_short_string_1, _medium_string_1)

    def time_short_long(self):
        self.editex.get_raw_score(_short_string_1, _long_string_1)

    def time_medium_long(self):
        self.editex.get_raw_score(_medium_string_1, _long_string_1)


class TimeLevenshtein:
    def setup(self):
        self.levenshtein = Levenshtein()

    def time_short_short(self):
        self.levenshtein.get_raw_score(_short_string_1, _short_string_2)

    def time_medium_medium(self):
        self.levenshtein.get_raw_score(_medium_string_1, _medium_string_2)

    def time_long_long(self):
        self.levenshtein.get_raw_score(_long_string_1, _long_string_2)

    def time_short_medium(self):
        self.levenshtein.get_raw_score(_short_string_1, _medium_string_1)

    def time_short_long(self):
        self.levenshtein.get_raw_score(_short_string_1, _long_string_1)

    def time_medium_long(self):
        self.levenshtein.get_raw_score(_medium_string_1, _long_string_1)


class TimeBagDistance:
    def setup(self):
        self.bag_distance = BagDistance()

    def time_short_short(self):
        self.bag_distance.get_raw_score(_short_string_1, _short_string_2)

    def time_medium_medium(self):
        self.bag_distance.get_raw_score(_medium_string_1, _medium_string_2)

    def time_long_long(self):
        self.bag_distance.get_raw_score(_long_string_1, _long_string_2)

    def time_short_medium(self):
        self.bag_distance.get_raw_score(_short_string_1, _medium_string_1)

    def time_short_long(self):
        self.bag_distance.get_raw_score(_short_string_1, _long_string_1)

    def time_medium_long(self):
        self.bag_distance.get_raw_score(_medium_string_1, _long_string_1)


class TimeNeedlemanWunsch:
    def setup(self):
        self.needleman_wunsch = NeedlemanWunsch()

    def time_short_short(self):
        self.needleman_wunsch.get_raw_score(_short_string_1, _short_string_2)

    def time_medium_medium(self):
        self.needleman_wunsch.get_raw_score(_medium_string_1, _medium_string_2)

    def time_long_long(self):
        self.needleman_wunsch.get_raw_score(_long_string_1, _long_string_2)

    def time_short_medium(self):
        self.needleman_wunsch.get_raw_score(_short_string_1, _medium_string_1)

    def time_short_long(self):
        self.needleman_wunsch.get_raw_score(_short_string_1, _long_string_1)

    def time_medium_long(self):
        self.needleman_wunsch.get_raw_score(_medium_string_1, _long_string_1)


class TimeSmithWaterman:
    def setup(self):
        self.smith_waterman = SmithWaterman()

    def time_short_short(self):
        self.smith_waterman.get_raw_score(_short_string_1, _short_string_2)

    def time_medium_medium(self):
        self.smith_waterman.get_raw_score(_medium_string_1, _medium_string_2)

    def time_long_long(self):
        self.smith_waterman.get_raw_score(_long_string_1, _long_string_2)

    def time_short_medium(self):
        self.smith_waterman.get_raw_score(_short_string_1, _medium_string_1)

    def time_short_long(self):
        self.smith_waterman.get_raw_score(_short_string_1, _long_string_1)

    def time_medium_long(self):
        self.smith_waterman.get_raw_score(_medium_string_1, _long_string_1)

class TimeSoundex:
    def setup(self):
        self.soundex = Soundex()

    def time_short_short(self):
        self.soundex.get_raw_score(_short_string_1, _short_string_2)

    def time_medium_medium(self):
        self.soundex.get_raw_score(_medium_string_1, _medium_string_2)

    def time_long_long(self):
        self.soundex.get_raw_score(_long_string_1, _long_string_2)

    def time_short_medium(self):
        self.soundex.get_raw_score(_short_string_1, _medium_string_1)

    def time_short_long(self):
        self.soundex.get_raw_score(_short_string_1, _long_string_1)

    def time_medium_long(self):
        self.soundex.get_raw_score(_medium_string_1, _long_string_1)


class TimeCosine:
    def setup(self):
        self.cosine = Cosine()

    def time_small_small_wo_rep(self):
        self.cosine.get_raw_score(_small_num_tokens_wo_rep, _small_num_tokens_wo_rep)

    def time_small_small_wi_rep(self):
        self.cosine.get_raw_score(_small_num_tokens_wi_rep, _small_num_tokens_wi_rep)

    def time_medium_medium_wo_rep(self):
        self.cosine.get_raw_score(_med_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_medium_medium_wi_rep(self):
        self.cosine.get_raw_score(_med_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_large_large_wo_rep(self):
        self.cosine.get_raw_score(_large_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_large_large_wi_rep(self):
        self.cosine.get_raw_score(_large_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_small_medium_wo_rep(self):
        self.cosine.get_raw_score(_small_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_small_medium_wi_rep(self):
        self.cosine.get_raw_score(_small_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_small_large_wo_rep(self):
        self.cosine.get_raw_score(_small_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_small_large_wi_rep(self):
        self.cosine.get_raw_score(_small_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_medium_large_wo_rep(self):
        self.cosine.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_medium_large_wi_rep(self):
        self.cosine.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)


class TimeDice:
    def setup(self):
        self.dice = Dice()

    def time_small_small_wo_rep(self):
        self.dice.get_raw_score(_small_num_tokens_wo_rep, _small_num_tokens_wo_rep)

    def time_small_small_wi_rep(self):
        self.dice.get_raw_score(_small_num_tokens_wi_rep, _small_num_tokens_wi_rep)

    def time_medium_medium_wo_rep(self):
        self.dice.get_raw_score(_med_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_medium_medium_wi_rep(self):
        self.dice.get_raw_score(_med_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_large_large_wo_rep(self):
        self.dice.get_raw_score(_large_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_large_large_wi_rep(self):
        self.dice.get_raw_score(_large_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_small_medium_wo_rep(self):
        self.dice.get_raw_score(_small_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_small_medium_wi_rep(self):
        self.dice.get_raw_score(_small_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_small_large_wo_rep(self):
        self.dice.get_raw_score(_small_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_small_large_wi_rep(self):
        self.dice.get_raw_score(_small_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_medium_large_wo_rep(self):
        self.dice.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_medium_large_wi_rep(self):
        self.dice.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)


class TimeJaccard:
    def setup(self):
        self.jaccard = Jaccard()

    def time_small_small_wo_rep(self):
        self.jaccard.get_raw_score(_small_num_tokens_wo_rep, _small_num_tokens_wo_rep)

    def time_small_small_wi_rep(self):
        self.jaccard.get_raw_score(_small_num_tokens_wi_rep, _small_num_tokens_wi_rep)

    def time_medium_medium_wo_rep(self):
        self.jaccard.get_raw_score(_med_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_medium_medium_wi_rep(self):
        self.jaccard.get_raw_score(_med_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_large_large_wo_rep(self):
        self.jaccard.get_raw_score(_large_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_large_large_wi_rep(self):
        self.jaccard.get_raw_score(_large_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_small_medium_wo_rep(self):
        self.jaccard.get_raw_score(_small_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_small_medium_wi_rep(self):
        self.jaccard.get_raw_score(_small_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_small_large_wo_rep(self):
        self.jaccard.get_raw_score(_small_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_small_large_wi_rep(self):
        self.jaccard.get_raw_score(_small_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_medium_large_wo_rep(self):
        self.jaccard.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_medium_large_wi_rep(self):
        self.jaccard.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)


class TimeGeneralizedJaccard:
    def setup(self):
        self.generalized_jaccard = GeneralizedJaccard()

    def time_small_small_wo_rep(self):
        self.generalized_jaccard.get_raw_score(_small_num_tokens_wo_rep, _small_num_tokens_wo_rep)

    def time_small_small_wi_rep(self):
        self.generalized_jaccard.get_raw_score(_small_num_tokens_wi_rep, _small_num_tokens_wi_rep)

    def time_medium_medium_wo_rep(self):
        self.generalized_jaccard.get_raw_score(_med_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_medium_medium_wi_rep(self):
        self.generalized_jaccard.get_raw_score(_med_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_large_large_wo_rep(self):
        self.generalized_jaccard.get_raw_score(_large_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_large_large_wi_rep(self):
        self.generalized_jaccard.get_raw_score(_large_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_small_medium_wo_rep(self):
        self.generalized_jaccard.get_raw_score(_small_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_small_medium_wi_rep(self):
        self.generalized_jaccard.get_raw_score(_small_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_small_large_wo_rep(self):
        self.generalized_jaccard.get_raw_score(_small_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_small_large_wi_rep(self):
        self.generalized_jaccard.get_raw_score(_small_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_medium_large_wo_rep(self):
        self.generalized_jaccard.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_medium_large_wi_rep(self):
        self.generalized_jaccard.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)


class TimeOverlap:
    def setup(self):
        self.ov_coeff = OverlapCoefficient()

    def time_small_small_wo_rep(self):
        self.ov_coeff.get_raw_score(_small_num_tokens_wo_rep, _small_num_tokens_wo_rep)

    def time_small_small_wi_rep(self):
        self.ov_coeff.get_raw_score(_small_num_tokens_wi_rep, _small_num_tokens_wi_rep)

    def time_medium_medium_wo_rep(self):
        self.ov_coeff.get_raw_score(_med_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_medium_medium_wi_rep(self):
        self.ov_coeff.get_raw_score(_med_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_large_large_wo_rep(self):
        self.ov_coeff.get_raw_score(_large_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_large_large_wi_rep(self):
        self.ov_coeff.get_raw_score(_large_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_small_medium_wo_rep(self):
        self.ov_coeff.get_raw_score(_small_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_small_medium_wi_rep(self):
        self.ov_coeff.get_raw_score(_small_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_small_large_wo_rep(self):
        self.ov_coeff.get_raw_score(_small_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_small_large_wi_rep(self):
        self.ov_coeff.get_raw_score(_small_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_medium_large_wo_rep(self):
        self.ov_coeff.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_medium_large_wi_rep(self):
        self.ov_coeff.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)


class TimeMongeElkan:
    def setup(self):
        self.monge_elkan = MongeElkan()

    def time_small_small_wo_rep(self):
        self.monge_elkan.get_raw_score(_small_num_tokens_wo_rep, _small_num_tokens_wo_rep)

    def time_small_small_wi_rep(self):
        self.monge_elkan.get_raw_score(_small_num_tokens_wi_rep, _small_num_tokens_wi_rep)

    def time_medium_medium_wo_rep(self):
        self.monge_elkan.get_raw_score(_med_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_medium_medium_wi_rep(self):
        self.monge_elkan.get_raw_score(_med_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_large_large_wo_rep(self):
        self.monge_elkan.get_raw_score(_large_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_large_large_wi_rep(self):
        self.monge_elkan.get_raw_score(_large_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_small_medium_wo_rep(self):
        self.monge_elkan.get_raw_score(_small_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_small_medium_wi_rep(self):
        self.monge_elkan.get_raw_score(_small_num_tokens_wi_rep, _med_num_tokens_wi_rep)


class TimeTfIdf:
    def setup(self):
        self.tfidf = TfIdf()
        self.tfidf_with_dampen = TfIdf(dampen=True)

        corpus_list = [_small_num_tokens_wo_rep, _small_num_tokens_wi_rep,
                       _med_num_tokens_wi_rep, _med_num_tokens_wo_rep,
                       _large_num_tokens_wo_rep, _large_num_tokens_wi_rep]
        self.tfidf_with_corpus = TfIdf(corpus_list)
        self.tfidf_with_corpus_dampen = TfIdf(corpus_list, dampen=True)

    def time_small_small_wo_rep_no_corpus_no_dampen(self):
        self.tfidf.get_raw_score(_small_num_tokens_wo_rep, _small_num_tokens_wo_rep)

    def time_small_small_wi_rep_no_corpus_no_dampen(self):
        self.tfidf.get_raw_score(_small_num_tokens_wi_rep, _small_num_tokens_wi_rep)

    def time_medium_medium_wo_rep_no_corpus_no_dampen(self):
        self.tfidf.get_raw_score(_med_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_medium_medium_wi_rep_no_corpus_no_dampen(self):
        self.tfidf.get_raw_score(_med_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_large_large_wo_rep_no_corpus_no_dampen(self):
        self.tfidf.get_raw_score(_large_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_large_large_wi_rep_no_corpus_no_dampen(self):
        self.tfidf.get_raw_score(_large_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_small_medium_wo_rep_no_corpus_no_dampen(self):
        self.tfidf.get_raw_score(_small_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_small_medium_wi_rep_no_corpus_no_dampen(self):
        self.tfidf.get_raw_score(_small_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_small_large_wo_rep_no_corpus_no_dampen(self):
        self.tfidf.get_raw_score(_small_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_small_large_wi_rep_no_corpus_no_dampen(self):
        self.tfidf.get_raw_score(_small_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_medium_large_wo_rep_no_corpus_no_dampen(self):
        self.tfidf.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_medium_large_wi_rep_no_corpus_no_dampen(self):
        self.tfidf.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    # dampen - true
    def time_small_small_wo_rep_no_corpus(self):
        self.tfidf_with_dampen.get_raw_score(_small_num_tokens_wo_rep, _small_num_tokens_wo_rep)

    def time_small_small_wi_rep_no_corpus(self):
        self.tfidf_with_dampen.get_raw_score(_small_num_tokens_wi_rep, _small_num_tokens_wi_rep)

    def time_medium_medium_wo_rep_no_corpus(self):
        self.tfidf_with_dampen.get_raw_score(_med_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_medium_medium_wi_rep_no_corpus(self):
        self.tfidf_with_dampen.get_raw_score(_med_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_large_large_wo_rep_no_corpus(self):
        self.tfidf_with_dampen.get_raw_score(_large_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_large_large_wi_rep_no_corpus(self):
        self.tfidf_with_dampen.get_raw_score(_large_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_small_medium_wo_rep_no_corpus(self):
        self.tfidf_with_dampen.get_raw_score(_small_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_small_medium_wi_rep_no_corpus(self):
        self.tfidf_with_dampen.get_raw_score(_small_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_small_large_wo_rep_no_corpus(self):
        self.tfidf_with_dampen.get_raw_score(_small_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_small_large_wi_rep_no_corpus(self):
        self.tfidf_with_dampen.get_raw_score(_small_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_medium_large_wo_rep_no_corpus(self):
        self.tfidf_with_dampen.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_medium_large_wi_rep_no_corpus(self):
        self.tfidf_with_dampen.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    # corpus list - true
    def time_small_small_wo_rep_no_dampen(self):
        self.tfidf_with_corpus.get_raw_score(_small_num_tokens_wo_rep, _small_num_tokens_wo_rep)

    def time_small_small_wi_rep_no_dampen(self):
        self.tfidf_with_corpus.get_raw_score(_small_num_tokens_wi_rep, _small_num_tokens_wi_rep)

    def time_medium_medium_wo_rep_no_dampen(self):
        self.tfidf_with_corpus.get_raw_score(_med_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_medium_medium_wi_rep_no_dampen(self):
        self.tfidf_with_corpus.get_raw_score(_med_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_large_large_wo_rep_no_dampen(self):
        self.tfidf_with_corpus.get_raw_score(_large_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_large_large_wi_rep_no_dampen(self):
        self.tfidf_with_corpus.get_raw_score(_large_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_small_medium_wo_rep_no_dampen(self):
        self.tfidf_with_corpus.get_raw_score(_small_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_small_medium_wi_rep_no_dampen(self):
        self.tfidf_with_corpus.get_raw_score(_small_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_small_large_wo_rep_no_dampen(self):
        self.tfidf_with_corpus.get_raw_score(_small_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_small_large_wi_rep_no_dampen(self):
        self.tfidf_with_corpus.get_raw_score(_small_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_medium_large_wo_rep_no_dampen(self):
        self.tfidf_with_corpus.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_medium_large_wi_rep_no_dampen(self):
        self.tfidf_with_corpus.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    # corpus list - true, dampen_true
    def time_small_small_wo_rep(self):
        self.tfidf_with_corpus_dampen.get_raw_score(_small_num_tokens_wo_rep, _small_num_tokens_wo_rep)

    def time_small_small_wi_rep(self):
        self.tfidf_with_corpus_dampen.get_raw_score(_small_num_tokens_wi_rep, _small_num_tokens_wi_rep)

    def time_medium_medium_wo_rep(self):
        self.tfidf_with_corpus_dampen.get_raw_score(_med_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_medium_medium_wi_rep(self):
        self.tfidf_with_corpus_dampen.get_raw_score(_med_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_large_large_wo_rep(self):
        self.tfidf_with_corpus_dampen.get_raw_score(_large_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_large_large_wi_rep(self):
        self.tfidf_with_corpus_dampen.get_raw_score(_large_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_small_medium_wo_rep(self):
        self.tfidf_with_corpus_dampen.get_raw_score(_small_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_small_medium_wi_rep(self):
        self.tfidf_with_corpus_dampen.get_raw_score(_small_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_small_large_wo_rep(self):
        self.tfidf_with_corpus_dampen.get_raw_score(_small_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_small_large_wi_rep(self):
        self.tfidf_with_corpus_dampen.get_raw_score(_small_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_medium_large_wo_rep(self):
        self.tfidf_with_corpus_dampen.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_medium_large_wi_rep(self):
        self.tfidf_with_corpus_dampen.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)


class TimeSoftTfIdf:
    def setup(self):
        self.soft_tfidf = SoftTfIdf()

        corpus_list = [_small_num_tokens_wo_rep, _small_num_tokens_wi_rep,
                       _med_num_tokens_wi_rep, _med_num_tokens_wo_rep,
                       _large_num_tokens_wo_rep, _large_num_tokens_wi_rep]
        self.soft_tfidf_with_corpus = SoftTfIdf(corpus_list)

    # no corpus list
    def time_small_small_wo_rep_no_corpus(self):
        self.soft_tfidf.get_raw_score(_small_num_tokens_wo_rep, _small_num_tokens_wo_rep)

    def time_small_small_wi_rep_no_corpus(self):
        self.soft_tfidf.get_raw_score(_small_num_tokens_wi_rep, _small_num_tokens_wi_rep)

    def time_medium_medium_wo_rep_no_corpus(self):
        self.soft_tfidf.get_raw_score(_med_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_medium_medium_wi_rep_no_corpus(self):
        self.soft_tfidf.get_raw_score(_med_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_large_large_wo_rep_no_corpus(self):
        self.soft_tfidf.get_raw_score(_large_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_large_large_wi_rep_no_corpus(self):
        self.soft_tfidf.get_raw_score(_large_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_small_medium_wo_rep_no_corpus(self):
        self.soft_tfidf.get_raw_score(_small_num_tokens_wo_rep, _med_num_tokens_wo_rep)

    def time_small_medium_wi_rep_no_corpus(self):
        self.soft_tfidf.get_raw_score(_small_num_tokens_wi_rep, _med_num_tokens_wi_rep)

    def time_small_large_wo_rep_no_corpus(self):
        self.soft_tfidf.get_raw_score(_small_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_small_large_wi_rep_no_corpus(self):
        self.soft_tfidf.get_raw_score(_small_num_tokens_wi_rep, _large_num_tokens_wi_rep)

    def time_medium_large_wo_rep(self):
        self.soft_tfidf_with_corpus.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)

    def time_medium_large_wi_rep(self):
        self.soft_tfidf_with_corpus.get_raw_score(_med_num_tokens_wo_rep, _large_num_tokens_wo_rep)

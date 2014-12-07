import numpy as np
from itertools import combinations_with_replacement
from future.moves.itertools import filterfalse

def ratio_to_cents(hz):
    '''Converts to cents.'''
    return np.log2(hz) * 1200.0

# Ideal intervals and triads
JUST_MAJOR_THIRD = ratio_to_cents(np.array([5./4.]))
JUST_MINOR_THIRD = ratio_to_cents(np.array([6./5.]))
JUST_PERFECT_FIFTH = ratio_to_cents(np.array([3./2.]))
JUST_MAJOR_TRIAD = np.array([JUST_MAJOR_THIRD, JUST_PERFECT_FIFTH, JUST_MINOR_THIRD]).ravel()
JUST_MINOR_TRIAD = np.array([JUST_MINOR_THIRD, JUST_PERFECT_FIFTH, JUST_MAJOR_THIRD]).ravel()
CHROMATIC_SEMITONE = np.array([76.0])
DIATONIC_SEMITONE = np.array([117.1])

# Ideal diatonic scale constructions
MAJOR_IDEALS = np.array([JUST_MAJOR_TRIAD, JUST_MINOR_TRIAD, JUST_MINOR_TRIAD, JUST_MAJOR_TRIAD, JUST_MAJOR_TRIAD, JUST_MINOR_TRIAD])
MAJOR_DEGREES = np.array([[0, 4, 7], [2, 5, 9], [4, 7, 11], [5, 9, 12], [7, 11, 14], [9, 12, 16]])

# Ideal meantone constructions of major and minor semitones
SEMITONE_DEGREES = np.array([[0, 1], [2, 3], [4, 5], [5, 6], [7, 8], [9, 10], [11, 12]])
MEANTONE_SEMITONES = np.array([CHROMATIC_SEMITONE, DIATONIC_SEMITONE, DIATONIC_SEMITONE, CHROMATIC_SEMITONE, CHROMATIC_SEMITONE, DIATONIC_SEMITONE, DIATONIC_SEMITONE])

# Ideal tonics
TONIC_THIRD_DEGREES = np.array([[0, 4]])
TONIC_THIRD_IDEAL = np.array([JUST_MINOR_THIRD])
TONIC_FIFTH_DEGREES = np.array([[0, 7]])
TONIC_FIFTH_IDEAL = np.array([JUST_PERFECT_FIFTH])

# Some temperaments under consideration
EQUAL_TEMPERAMENT = np.array([0., 100., 200., 300., 400., 500., 600., 700., 800., 900., 1000., 1100.])
WERCK_III = np.array([0.0, 90.226, 192.180, 294.135, 390.225, 498.045, 588.045, 696.090, 792.181, 888.270, 996.090, 1092.180])
WERCK_IV = np.array([0.0, 82.406, 196.090, 294.135, 392.180, 498.045, 588.270, 694.135, 784.361, 890.225, 1003.910, 1086.315])
ACS_I = np.array([0.0, 90.1, 190.5, 282.3, 386.0, 498.5, 586.1, 698.2, 777.9, 883.6, 992.3, 1083.7])
ACS_II = np.array([0.0, 84.8, 192.8, 295.9, 386.7, 504.1, 588.9, 695.9, 790.7, 888.7, 1001.9, 1087.9])
MEANTONE = np.array([0.0, 76, 193, 310, 386, 503, 579, 697, 773, 890, 1007, 1083])

def mean_tempering(actual, ideal = JUST_MAJOR_TRIAD, **kwargs):
    '''Gets the mean tempering of a given collection of intervals.'''
    if 'weights' in kwargs:
        weights = kwargs['weights']
    else: 
        weights = np.ones(ideal.shape)
    return sum(abs(actual - ideal) * weights)

def combinatorial_difference(input):
    '''Gets the sequence of differences. This corresponds to the upper
    triangular portion of a difference matrix.'''
    combos = combinations_with_replacement(input, 2)
    diffs = map(lambda x: abs(x[0] - x[1]), combos)
    return list(filterfalse(lambda x: x == 0, diffs))

def key_tempering(tuning, intervals, ideals, **kwargs):
    '''Gets the mean tempering of an entire key.'''
    def correct_octaves(interval):
        addition = 0.0
        while(interval >= tuning.size):
            addition += 1200.0
            interval -= tuning.size
        return tuning[interval] + addition
    def get_diffs(pair):
        triad = np.array(combinatorial_difference(map(correct_octaves, pair[0])))
        ideal = np.array(pair[1])
        return mean_tempering(triad, ideal, **kwargs)
    return sum(map(get_diffs, zip(intervals, ideals))) / intervals.shape[0]


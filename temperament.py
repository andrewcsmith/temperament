import matplotlib.pyplot as plt
import numpy as np
import itertools

JUST_MAJOR_TRIAD = np.array([5./4., 3./2., 6./5.])
JUST_MINOR_TRIAD = np.array([6./5., 3./2., 5./4.])
EQUAL_TEMPERAMENT = np.array([0., 100., 200., 300., 400., 500., 600., 700., 800., 900., 1000., 1100.])

def hz_to_cents(hz):
    return np.log2(hz) * 1200.0

def mean_tempering(actual, ideal = hz_to_cents(JUST_MAJOR_TRIAD)):
    return sum(abs(actual - ideal))

def combinatorial_difference(input):
    combos = itertools.combinations_with_replacement(input, 2)
    diffs = map(lambda x: abs(x[0] - x[1]), combos)
    return list(itertools.filterfalse(lambda x: x == 0, diffs))

def key_tempering(tuning, intervals, ideals):
    def correct_octaves(interval):
        addition = 0.0
        while(interval >= tuning.size):
            addition += 1200.0
            interval -= tuning.size
        return tuning[interval] + addition
    def get_diffs(pair):
        triad = np.array(combinatorial_difference(map(correct_octaves, pair[0])))
        ideal = np.array(pair[1])
        return mean_tempering(triad, ideal)
    return sum(map(get_diffs, zip(intervals, ideals))) / intervals.shape[0]


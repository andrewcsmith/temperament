'''
Plotting the temperaments
'''
from temperament import *
import numpy as np
import matplotlib.pyplot as plt

circle_of_fifths = ['C', 'G', 'D', 'A', 'E', 'B', 'F#/Gb', 'C#/Db', 'G#/Eb', 'D#/Eb', 'A#/Bb', 'F']
order = [0, 7, 2, 9, 4, 11, 6, 1, 8, 3, 10, 5]

def key_tempering_for(tuning):
    return np.vectorize(lambda i: key_tempering(tuning, MAJOR_DEGREES +
        order[i], MAJOR_IDEALS))

def fifth_tempering_for(tuning):
    correct_octaves = correct_octaves_for(tuning)
    def fifth_tempering(i):
        degrees = TONIC_FIFTH_DEGREES + order[i]
        actual = combinatorial_difference(correct_octaves(degrees))
        return mean_tempering(actual, TONIC_FIFTH_IDEAL)
    return np.vectorize(fifth_tempering)

x = np.arange(0, 12, 1)
werck_iii = key_tempering_for(WERCK_III)(x)
werck_iv = key_tempering_for(WERCK_IV)(x)
meantone = key_tempering_for(MEANTONE)(x)
et = key_tempering_for(EQUAL_TEMPERAMENT)(x)
acs_i = key_tempering_for(ACS_I)(x)
acs_ii = key_tempering_for(ACS_II)(x)

plt.axis([0, 11, 0, 100])
plt.plot(x, werck_iii, 'r-o', x, werck_iv, 'g-o', x, meantone, 'b-o', x, et, 'k-o', x, acs_i, 'y-o', x, acs_ii, 'c-o')

# Set the axes markers
plt.xticks(x, circle_of_fifths)
plt.legend(['Werckmeister III', 'Werckmeister IV', 'Meantone', 'Equal Temperament', 'ACS I', 'ACS II'])

# Labels
plt.xlabel('tonic of key', fontsize=14, color='black')
plt.ylabel('mean tempering of key', fontsize=14, color='black')

plt.show()


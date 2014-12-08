'''
Plotting the temperaments
'''
from temperament import *
import numpy as np
import matplotlib.pyplot as plt

circle_of_fifths = ['C', 'G', 'D', 'A', 'E', 'B', 'F#/Gb', 'C#/Db', 'G#/Eb', 'D#/Eb', 'A#/Bb', 'F']
order = [0, 7, 2, 9, 4, 11, 6, 1, 8, 3, 10, 5]

x = np.arange(0, 12, 1)
weights = np.array([0.5, 1.0, 0.5])
weighted_fifth = lambda t: weighted_key_tempering_for(t, weights)

werck_iii = weighted_fifth(WERCK_III)(x)
werck_iv = weighted_fifth(WERCK_IV)(x)
meantone = weighted_fifth(MEANTONE)(x)
et = weighted_fifth(EQUAL_TEMPERAMENT)(x)
acs_i = weighted_fifth(ACS_I)(x)
acs_ii = weighted_fifth(ACS_II)(x)

plt.axis([0, 11, 0, 100])
plt.plot(x, werck_iii, 'r-<', 
        x, werck_iv, 'g->', 
        x, meantone, 'b-o', 
        x, et, 'k-x', 
        x, acs_i, 'y-d', 
        x, acs_ii, 'c-D')

# Set the axes markers
plt.xticks(x, circle_of_fifths)
plt.legend(['Werckmeister III', 'Werckmeister IV', 'Meantone', 'Equal Temperament', 'ACS I', 'ACS II'])

# Labels
plt.title('Figure 2: Weighted mean tempering of diatonic triads')
plt.xlabel('Tonic of key', fontsize=14, color='black')
plt.ylabel('Weighted tempering of key', fontsize=14, color='black')

plt.show()


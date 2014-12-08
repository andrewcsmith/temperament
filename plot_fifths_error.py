'''
Plotting the temperaments
'''
from temperament import *
import numpy as np
import matplotlib.pyplot as plt

circle_of_fifths = ['C', 'G', 'D', 'A', 'E', 'B', 'F#/Gb', 'C#/Db', 'G#/Eb', 'D#/Eb', 'A#/Bb', 'F']
order = [0, 7, 2, 9, 4, 11, 6, 1, 8, 3, 10, 5]

x = np.arange(0, 12, 1)
werck_iii = fifth_tempering_for(WERCK_III)(x)
werck_iv = fifth_tempering_for(WERCK_IV)(x)
meantone = fifth_tempering_for(MEANTONE)(x)
et = fifth_tempering_for(EQUAL_TEMPERAMENT)(x)

plt.axis([0, 11, 0, 15])
plt.plot(x, werck_iii, 'r-o', x, werck_iv, 'g-o', x, meantone, 'b-o', x, et, 'k-o')

# Set the axes markers
plt.xticks(x, circle_of_fifths)
plt.legend(['Werckmeister III', 'Werckmeister IV', 'Meantone', 'Equal Temperament'])

# Labels
plt.xlabel('tonic of key', fontsize=14, color='black')
plt.ylabel('mean tempering of key', fontsize=14, color='black')

plt.show()


'''
Plotting the temperaments
'''
from temperament import *
import numpy as np
import matplotlib.pyplot as plt

circle_of_fifths = ['C', 'G', 'D', 'A', 'E', 'B', 'F#/Gb', 'C#/Db', 'G#/Eb', 'D#/Eb', 'A#/Bb', 'F']
order = [0, 7, 2, 9, 4, 11, 6, 1, 8, 3, 10, 5]

def get_tempering(tuning):
    return lambda i: key_tempering(tuning, MAJOR_DEGREES + order[i], MAJOR_IDEALS)

x = np.arange(0, 12, 1)
werck_iii = list(map(get_tempering(WERCK_III), x))
werck_iv = list(map(get_tempering(WERCK_IV), x))
meantone = list(map(get_tempering(MEANTONE), x))
et = list(map(get_tempering(EQUAL_TEMPERAMENT), x))

plt.axis([0, 11, 0, 100])
plt.plot(x, werck_iii, 'ro', x, werck_iv, 'go', x, meantone, 'bo', x, et, 'ko')

# Set the axes markers
plt.xticks(x, circle_of_fifths)
plt.legend(['Werckmeister III', 'Werckmeister IV', 'Meantone', 'Equal Temperament'])

# Labels
plt.xlabel('tonic of key', fontsize=14, color='black')
plt.ylabel('mean tempering of key', fontsize=14, color='black')

plt.show()


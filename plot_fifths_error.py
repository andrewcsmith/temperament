'''
Plotting the temperaments
'''
from temperament import *
import numpy as np
import matplotlib.pyplot as plt

circle_of_fifths = ['C', 'G', 'D', 'A', 'E', 'B', 'F#/Gb', 'C#/Db', 'G#/Eb', 'D#/Eb', 'A#/Bb', 'F']
order = [0, 7, 2, 9, 4, 11, 6, 1, 8, 3, 10, 5]

x = np.arange(0, 12, 1)
werck_iii_fifth = fifth_tempering_for(WERCK_III)(x)
werck_iv_fifth = fifth_tempering_for(WERCK_IV)(x)
meantone_fifth = fifth_tempering_for(MEANTONE)(x)
et_fifth = fifth_tempering_for(EQUAL_TEMPERAMENT)(x)
acs_i_fifth = fifth_tempering_for(ACS_I)(x)
acs_ii_fifth = fifth_tempering_for(ACS_II)(x)

plt.axis([0, 11, 0, 50])
plt.plot(x, werck_iii_fifth, 'r-<',
        x, werck_iv_fifth, 'g->', 
        x, meantone_fifth, 'b-o', 
        x, et_fifth, 'k-x',
        x, acs_i_fifth, 'y-d', 
        x, acs_ii_fifth, 'c-D')

# Set the axes markers
plt.xticks(x, circle_of_fifths)
plt.legend(['Werckmeister III', 'Werckmeister IV', 'Meantone', 'Equal Temperament', 'ACS I', 'ACS II'])

# Labels
plt.title('Figure 4: Tempering of fifths')
plt.xlabel('Tonic of key', fontsize=14, color='black')
plt.ylabel('Tempering of tonic fifth', fontsize=14, color='black')

plt.show()


"""
Created on 08/28/2019
Author: William Long
"""

import numpy as np
import matplotlib.pyplot as plt

"""
This program should graph the Sine and Cosine fuactions.
"""


"""This sets up the lists for the X axis, Sine graph, and Cosine graph."""
points = 1000  # number of points on the X-axis.
X = np.linspace(0, 2*np.pi, points)
S = [np.sin(x) for x in X]
C = [np.cos(x) for x in X]

# adding Tangent with cut-off limit on y-axis
T = [min(4, max(-4, np.tan(x))) for x in X] 


'''This part actually makes the graph.'''
plt.subplot(221)
plt.plot(X, S, 'b-.', lw=2.5, label='Sine')
plt.plot(X, C, 'r', lw=2.5, label='Cosine')
plt.plot(X, T, 'g--', lw = 2.5, label = 'Tangent')

plt.grid(True)
plt.legend(loc=0)
plt.show()

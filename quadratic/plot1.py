#!/bin/python3
import matplotlib.pyplot as plt
import numpy

P0 = (0, 1)
plt.scatter(P0[0], P0[1])

P1 = (3, 2)
plt.scatter(P1[0], P1[1])

P2 = (5, 1)
plt.scatter(P2[0], P2[1])

PX = [(1-t)*((1-t)*P0[0]+t*P1[0]) + t*((1-t)*P1[0]+t*P2[0]) for t in numpy.arange(float(0), float(1), 0.01)]
PY = [(1-t)*((1-t)*P0[1]+t*P1[1]) + t*((1-t)*P1[1]+t*P2[1]) for t in numpy.arange(float(0), float(1), 0.01)]

plt.plot(PX, PY)
plt.show()

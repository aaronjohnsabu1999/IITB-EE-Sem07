from numpy.random import multivariate_normal as mNormal
import matplotlib.pyplot as plt

mean = [-5.0, -5.0]
cov = [[1, 0], [0, 1]]

samples = mNormal(mean, cov, 100000)
x = samples.T[0]
y = samples.T[1]
deltas = [((x[i]-mean[0])**2 + (y[i]-mean[1])**2)**0.5 for i in range(len(samples))]

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(x, y)
ax2.hist(deltas, 100)

plt.show()
import numpy as np

city = np.array(["New Orleans", "Inglewood", "Glendale", "Las Vegas", "Santa Clara", "Atlanta", "Cleveland", "Cincinnati", "Buffalo"])

reg = lambda x: (1 - np.tanh(40 * x - 2)) / 2

baseline = np.array([150000, 2, 450, 16000])

temp = np.array([12.8, 14.5, 30.9, 27.2, 12, 10.5, 1, 1.7, 2.8])
loc = np.array([1.1, 1.8, 1.6, 1.2, 1.5, 0.9, 1.01, 0.66, 6])
trans = np.array([83.7, 80, 77.5, 85, 82.4, 98, 81, 80.3, 78.4])
energy = np.array([43, 68, 44.9, 53.4, 76.9, 62, 68.8, 82.9, 50.7])
landfill = np.array([97, 92, 81, 76, 68, 77, 96, 77.8, 70])
res = np.array([149000000, 5940000, 13500000, 356000000, 11000000, 147000000, 513000000, 132000000, 160000000])
neutralization = np.array([74550 / 365, 21000 / 365, 38325 / 365, 124250 / 365, 24850 / 365, 95813 / 365, 270, 680, 140])

# water
alpha = 3.5
water = reg(alpha * temp / temp[0] * baseline[0] / res)
print(list(water))

# waste
alpha = 0.2
waste = (alpha * temp[2] * landfill / 100 + (1 - alpha) * temp[1] * landfill / 100) * -1
print(list(waste))

# gas
alpha = 0.79
beta = 1.1
theta = 1.4
emission = reg(alpha * loc / loc[0] * beta * trans / trans[0] * theta * energy / energy[0] / neutralization)
print(list(emission))

res = []
for i in range(len(water)):
    res.append([water[i], waste[i], emission[i]])

print(res)

import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, x_val):
    n = len(x)
    p = 0
    for i in range(n):
        term = 1
        for j in range(n):
            if i != j:
                term *= (x_val - x[j]) / (x[i] - x[j])
        p += y[i] * term    
    return p

temperature = np.array([0, 20, 40, 60, 80, 100])
pressure = np.array([1.000, 0.889, 0.745, 0.582, 0.412, 0.248])

temperatures_to_interpolate = np.array([10, 30, 50, 70, 90])
pressures_interpolated = lagrange_interpolation(temperature, pressure, temperatures_to_interpolate)

# plot
plt.plot(temperature, pressure, '*', color='red', label='Data points', markersize = 15)
plt.plot(temperatures_to_interpolate, pressures_interpolated, '-', color='black', label='Interpolated')
plt.xlabel('Temperature (°C)')
plt.ylabel('Pressure (atm)')
plt.legend()
plt.show()
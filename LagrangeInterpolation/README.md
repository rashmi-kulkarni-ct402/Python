# Lagrange Interpolation

Interpolation is a method in mathematics and computational science used to estimate values between known data points. Lagrange interpolation is a polynomial interpolation method that constructs a polynomial function that passes through a given set of data points. It is named after the mathematician Joseph-Louis Lagrange.

## Lagrange Interpolation Formula

Given (n) data points ((x_i, y_i)), where (i = 0, 1, 2, ..., n-1), the Lagrange interpolation polynomial (P(x)) is given by:

\[ P(x) = \sum_{i=0}^{n-1} y_i \cdot l_i(x) \]

where (l_i(x)) are the Lagrange basis polynomials defined as:

\[ l_i(x) = \prod_{j=0, j \neq i}^{n-1} \frac{x - x_j}{x_i - x_j} \]

## Explanation of Code

The provided Python code demonstrates Lagrange interpolation to estimate pressure values at given temperature points. 

- Import Libraries: NumPy is used for numerical operations, and Matplotlib is used for plotting.
- `lagrange Interpolation` Function: The lagrange_interpolation function takes arrays x and y representing the known data points and a value x_val for which the interpolated value is desired. It returns the interpolated value at x_val.
- Known Data Points: Arrays `temperature` and `pressure` contain the known data points, where temperature represents the temperature values (in °C) and pressure represents the corresponding pressure values (in atm).
- Interpolation of Pressure Values: The temperatures_to_interpolate array contains the temperatures (in °C) for which pressure values need to be interpolated. The lagrange_interpolation function is used to interpolate the pressure values for these temperatures.
- Plotting Data: The known data points are plotted as red asterisks, and the interpolated points are plotted as a black line on a temperature-pressure graph.
- Visualization: The resulting plot visualizes the pressure-temperature relationship using Lagrange interpolation.


## Output

![LagrangeInterpolation](https://github.com/rashmi-kulkarni-ct402/Python/assets/158051740/d68da298-7741-4e25-8657-93c7822f2598)



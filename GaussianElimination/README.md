# Gaussian Elimination

Gaussian elimination is a method used to solve systems of linear equations. It simplifies a given system into an equivalent upper triangular system, making it easier to find the solution through back substitution.

## Gaussian Elimination Algorithm
- Input: A matrix 𝐴 representing the coefficients of the linear equations and a vector 𝑏 representing the constants.
- Augmented Matrix: Form the augmented matrix [𝐴∣𝑏].
- Forward Elimination: Convert the augmented matrix into upper triangular form using row operations (partial pivoting may be used for numerical stability).
- Backward Substitution: Solve the upper triangular system or the unknowns 𝑥𝑖, starting from the last equation.

## Explanation of Code
The provided Python code demonstrates Gaussian elimination to solve a system of linear equations given by the matrix 𝐴 and the constant vector 𝑏. 

- Input Matrices: The variable_matrix represents the coefficients of the linear equations, and the constant_matrix represents the constants.
- Initialization: Initialize an array x to store the solution vector.
- Augmented Matrix: Form the augmented matrix by concatenating variable_matrix and constant_matrix.
- Forward Elimination: Perform forward elimination to convert the augmented matrix to upper triangular form.
- Backward Substitution: Solve the upper triangular system for the unknowns using back substitution.
- Output: Print the solution vector x


## Output



import numpy as np

def gaussian_elimination(a_matrix, b_matrix):
    if a_matrix.shape[0] != a_matrix.shape[1]:
        print("ERROR: Square matrix not given!")
        return
    
    if b_matrix.shape[1] > 1 or b_matrix.shape[0] != a_matrix.shape[0]:
        print("ERROR: Constant vector incorrectly sized!")
        return

    # Initialization
    n = len(b_matrix)
    m = n - 1
    x = np.zeros(n)

    # Creation of augmented matrix
    augmented_matrix = np.concatenate((a_matrix, b_matrix), axis=1).astype(float)
    print("Initial augmented matrix:")
    print(augmented_matrix)
    print("Solving upper-triangular matrix - ")

    # Forward Elimination with partial pivoting
    for i in range(n):
        max_index = i
        max_val = augmented_matrix[i][i]
        for k in range(i+1, n):
            if abs(augmented_matrix[k][i]) > abs(max_val):
                max_val = augmented_matrix[k][i]
                max_index = k
        
        augmented_matrix[[i, max_index]] = augmented_matrix[[max_index, i]]

        if augmented_matrix[i][i] == 0.0:
            print("Divide by zero error")
            return
        
        for j in range(i + 1, n):
            scaling_factor = augmented_matrix[j][i] / augmented_matrix[i][i]
            augmented_matrix[j][i:] -= scaling_factor * augmented_matrix[i][i:]

    # Backward substitution
    if augmented_matrix[m][m] == 0:
        print("Divide by zero error")
        return
    
    x[m] = augmented_matrix[m][n] / augmented_matrix[m][m]

    for k in range(n - 2, -1, -1):
        x[k] = augmented_matrix[k][n]

        for j in range(k + 1, n):
            x[k] -= augmented_matrix[k][j] * x[j]
        
        x[k] /= augmented_matrix[k][k]

    # Display result
    print("Following x-vector matrix solves the augmented matrix: ")
    for answer in range(n):
        print(f"x{answer} is {x[answer]}")

variable_matrix = np.array([[2, 3, -1], [1, -1, 2], [3, 2, 1]])
constant_matrix = np.array([[7], [5], [12]])

gaussian_elimination(variable_matrix, constant_matrix)
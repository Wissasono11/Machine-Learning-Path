#bagaimana cara membuat matriks dengan kasus
"""
2 x [5  0] = [10  0]
    [1 -2]   [2  -4]
"""
matriks = [[5, 0],
           [1, -2]]
def_mat = [[0 for j in range (2)] for i in range(2)]

for i in range(len(matriks)):
    for j in range(len(matriks[0])):
        def_mat[i][j] = matriks[i][j]*2

print(def_mat)
"""
Output:
[[10, 0], [2, -4]]
"""
import numpy as np
var_mat = np.array([[5,0],
                   [1, -2]])

result = var_mat * 2
print(result)
"""
Output:
[[10  0]
 [ 2 -4]]
"""
import numpy as np
arr2d = np.array([[10, 60, 30], [80, 20, 50]])
print("Max:", np.max(arr2d))          # 80
print("Min:", np.min(arr2d))          # 10
print("Argmax:", np.argmax(arr2d))    # 3 (80 is at index 3 in flattened array)
print("Argmin:", np.argmin(arr2d))    # 0 (10 is at index 0)
# Argmax/Argmin along axis
print("Argmax along axis 0:", np.argmax(arr2d, axis=0))  # [1 0 1]
print("Argmin along axis 1:", np.argmin(arr2d, axis=1))  # [0 1]

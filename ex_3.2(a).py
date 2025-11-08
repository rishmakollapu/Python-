import numpy as np
arr = np.array([10, 20, 30, 40, 50])
specified_number = 30
less_than = arr[arr < specified_number]
greater_than = arr[arr > specified_number]
print("Less than 30:", less_than)
print("Greater than 30:", greater_than)


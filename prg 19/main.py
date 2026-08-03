"""
Write programs to create numpy arrays of different shapes and from different sources,
reshape and slice arrays, add array indexes, and apply arithmetic, logic, and aggregation
functions to some or all array elements.
"""

import numpy as np

arr1d = np.array([10, 20, 30, 40, 50])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
zeroArr = np.zeros((2, 3))
onesArr = np.ones((3, 2))
rangedArr = np.arange(1, 10, 2)
spacedArr = np.linspace(0, 1, 5)
identityArr = np.eye(3)

original = np.arange(1, 13)
reshaped2d = original.reshape(3, 4)
reshaped3d = original.reshape(2, 2, 3)
flattened = reshaped2d.flatten()

slice1d = arr1d[1:4]
subMatrix = reshaped2d[0:2, 1:3]
firstRow = reshaped2d[0, :]
lastCol = reshaped2d[:, -1]

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

added = a + b
subtracted = a - b
multiplied = a * b
divided = a / b
exponentiated = b ** 2

addIndexSum = a + np.arange(len(a))

gtFilter = a > 15
andLogic = (a > 15) & (b < 4)
orLogic = (a < 15) | (b == 4)
notLogic = ~(a == 20)
conditionalSelect = np.where(a > 20, a, 0)

totalSum = np.sum(reshaped2d)
columnSum = np.sum(reshaped2d, axis=0)
rowSum = np.sum(reshaped2d, axis=1)
meanVal = np.mean(reshaped2d)
maxVal = np.max(reshaped2d)
minVal = np.min(reshaped2d)
stdDev = np.std(reshaped2d)
cumulativeSum = np.cumsum(a)

print("1D Array:", arr1d)
print("2D Reshaped Matrix:\n", reshaped2d)
print("Sliced Sub-matrix:\n", subMatrix)
print("Arithmetic Addition:", added)
print("Array with Index Added:", addIndexSum)
print("Boolean Mask (a > 15):", gtFilter)
print("Conditional Select (where a > 20):", conditionalSelect)
print("Total Sum of 2D Matrix:", totalSum)
print("Column-wise Sum:", columnSum)
print("Row-wise Sum:", rowSum)
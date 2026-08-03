"""
Program to sort numbers in a List in Ascending Order using Bubble Sort by passing the List as 
argument to a function. 
"""

def bubbleSort(arr:list[int])->list[int]:
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] =arr[j],arr[i]
    return arr


numbers =  [int(x) for x in input("Enter numbers separated by space: ").split()]
print("Before sorting:")
print(*numbers)
print("After sorting:")
arr = bubbleSort(numbers)
print(*arr)
"""
Program to perform Linear Search in a List and Report Success or Failure. 
"""

def linearSearch(arr:list[int],target:int)->list[int]:
    for i in arr:
        if i == target:
            return True
    return False

numbers =  [int(x) for x in input("Enter numbers separated by space: ").split()]
tar = int(input("Enter the target element you want to search: "))

if linearSearch(numbers,tar) :
    print(f"Target {tar} is present.")
else:
    print(f"Target {tar} is absent.")

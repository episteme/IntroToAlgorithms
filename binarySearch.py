import math

def binSearch(A, v):
    left = 0
    right = len(A) - 1
    while(left < right):
        mid = left + (right - left) / 2
        if(A[mid] == v):
            return mid
        elif(A[mid] < v):
            left = mid + 1
        else:
            right = mid
    return -1

print(binSearch([1,3,4,5,9,10], 1))
print(binSearch([1,3,4,5,9,10], 3))
print(binSearch([1,3,4,5,9,10], 4))
print(binSearch([1,3,4,5,9,10], 5))
print(binSearch([1,3,4,5,9,10], 9))
print(binSearch([1,3,4,5,9,10], 10))
print(binSearch([1,3,4,5,9,10], 0))
print(binSearch([1,3,4,5,9,10], 11))

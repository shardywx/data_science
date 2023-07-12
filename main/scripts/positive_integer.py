def solution(A):
    """
    Find the smallest positive integer that doesn't exist in an array 
    """
    found = False
    n = len(A)
    for i in range(1, n+2):
        found = False 
        for j in range(n):
            if A[j] == i:
                found = True 
                break
        if found == False:
            return i

array = [1,2,3,4,6,1]
print(solution(array))
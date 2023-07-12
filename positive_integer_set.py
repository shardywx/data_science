def solution(A):
    """
    Find the smallest positive integer that doesn't exist in an array 
    """
    n = len(A)
    dict = set(A)
    for i in range(1, n+2):
        if i not in dict:
            return i

array = [1,2,4,1,-5,-2,7]
print(solution(array))
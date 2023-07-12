from typing import List

def solution(A: List):
    """
    Find the smallest positive integer that doesn't exist in an array 
    """
    n = len(A)
    dict = set(A)
    for i in range(1, n+2):
        if i not in dict:
            return i
        
if __name__ == "__main__":
    array = [1,2,3,5,1,-5,-2,7]
    smallest_integer = solution(array)
    print(smallest_integer)
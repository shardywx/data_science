from typing import List

def solution(integer_array: List):
    """
    Find the smallest positive integer that doesn't exist in an array 
    """
    n = len(integer_array)
    dict = set(integer_array)
    for i in range(1, n+2):
        if i not in dict:
            return i
        
def main(integer_array: List):
    """
    Entry point function for the code above
    """
    smallest_integer = solution(integer_array)
    return smallest_integer

if __name__ == "__main__":
    main()
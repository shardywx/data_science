from typing import List

def solution(integer_array: List):
    """
    Find the smallest positive integer that doesn't exist in an array 
    """
    for element in integer_array:
        if not (element > -1000000 and element < 1000000):
            print('Elements should be valued between -1000000 and 1000000')
            exit

    n = len(integer_array)
    if not n > 0 and n < 100000:
        print('integer array should have length between 1 and 100000')
        exit
    else:
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
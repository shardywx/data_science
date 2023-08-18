# Enter your code here. Read input from STDIN. Print output to STDOUT
# Problem defined here: https://www.hackerrank.com/challenges/exceptions/problem
# Task: You are given two values 'a' and 'b'. Perform integer division and print a/b. 
# The first line of input from stdin contains T, the number of test cases. The next T lines each contain
# the space separated values of a and b. 

def exceptions(a, b):

    try:
        print(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        print('Error Code:',e)
    
if __name__ == '__main__':

    T = int(input())
    for i in range(T):
        a, b = input().split()
        
        exceptions(a, b)

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Problem defined here: https://www.hackerrank.com/challenges/exceptions/problem

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

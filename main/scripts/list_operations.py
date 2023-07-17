# Problem at link (https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true)
# Initialise a list and perform a number of commands

if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        c=input().split()
        if c[0]=='insert':
            list.insert(int(c[1]),int(c[2]))
        elif c[0]=='print':
            print(list)
        elif c[0]=='remove':
            list.remove(int(c[1]))
        elif c[0]=='sort':
            list.sort()
        elif c[0]=='append':
            list.append(int(c[1]))
        elif c[0]=='pop':
            list.pop(-1)
        elif c[0]=='reverse':
            list.reverse()
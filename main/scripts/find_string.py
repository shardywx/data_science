# Following the example below
# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

def count_substring(string, sub_string):
    """
    Count the number of times a substring occurs within a longer string
    """
    length_diff = len(string) - len(sub_string)
    count = 0 
    for i in range(0, length_diff+1):
        shortened_string = string[0+i:len(sub_string)+i]
        if sub_string in shortened_string:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
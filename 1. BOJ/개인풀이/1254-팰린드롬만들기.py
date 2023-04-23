import sys

input = sys.stdin.readline

string = input().strip()
string_copy = string
n = len(string)
temp_str = ""
for i in range(n):
    isPalindrome = 1
    s, e = 0, len(string_copy)-1
    while s < e:
        if string_copy[s] != string_copy[e]:
            isPalindrome = 0
            break
        s += 1
        e -= 1

    if isPalindrome == 0:
        temp_str = string[i] + temp_str
        string_copy = string + temp_str
    else:
        break

print(len(string_copy))

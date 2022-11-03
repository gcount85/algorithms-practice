import random
NX = input()  # "10 5"
수열A = input()
n, x = NX.split(" ")
lst2 = 수열A.split(" ")
temp = [str(i) for i in lst2 if int(i) < int(x)]
answer = " ".join(temp)
print(answer)
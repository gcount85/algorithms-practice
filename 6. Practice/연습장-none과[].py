a = []
b = None


if a == []:     # true
    print("a는 []이다")
if a:           # false    
    print("a는 존재한다")
if a == None:   # false   
    print("a는 []이면서 None이다")
if b:           # false   
    print("b는 존재한다")
if b == []:     # false   
    print("b는 none이면서 []이다")

    
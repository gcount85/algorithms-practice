class MyClassA:
    def __init__(self, value):
        self.value = value

    def str(self):
        return f"MyClassA: {self.value}"


class MyClassB:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClassB: {self.value}"


a = MyClassA(5)
b = MyClassB(5)

print(a.str())  # Output: MyClassA: 5
print(str(a))  # Output: <__main__.MyClassA object at 0x7f8e291d76d0>
# 빌트인 str() 메소드를 사용하지 못함!

print(b.__str__())  # Output: MyClassB: 5
print(str(b))   # Output: MyClassB: 5

print(type([5].__str__()))  # str
print(type(str(5)))  # str

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        return NotImplemented


a = ComplexNumber(1, 2)
b = ComplexNumber(3, 4)

# `+` 연산자가 __add__ 메소드를 호출합니다.
c = a + b
# __add__ 메소드를 정의하지 않으면 뜨는 에러:
# TypeError: unsupported operand type(s) for +: 'ComplexNumber' and 'ComplexNumber'

print(c.real)  # 출력: 4
print(c.imag)  # 출력: 6

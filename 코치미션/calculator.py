import sys

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

def convert_to_postfix(S):
    opStack = ArrayStack()
    answer = ''
    
    for w in S :
        if w in prec :
            if opStack.isEmpty() :
                opStack.push(w)
            else :
                if w == '(' :
                    opStack.push(w)
                else :
                    while prec.get(w) <= prec.get(opStack.peek()) :
                        answer += opStack.pop()
                        if opStack.isEmpty() : break
                    opStack.push(w)
        elif w == ')' :
            while opStack.peek() != '(' :
                answer += opStack.pop()
            opStack.pop()
        else :
            answer += w
    
    while not opStack.isEmpty() :
        answer += opStack.pop()
    
    return answer

def calculate(tokens):
    stack = ArrayStack()
    for token in tokens:
        if token == '+':
            stack.push(stack.pop()+stack.pop())
        elif token == '-':
            stack.push(-(stack.pop()-stack.pop()))
        elif token == '*':
            stack.push(stack.pop()*stack.pop())
        elif token == '/':
            rv = stack.pop()
            stack.push(stack.pop()/rv)
        else:
            stack.push(int(token))
    return stack.pop()

infix = sys.stdin.readline().replace("\n", "").replace(" ","")

postfix = convert_to_postfix(infix)

print(f"postfix : {postfix}")

result = calculate(postfix)

print(f"result : {result}")






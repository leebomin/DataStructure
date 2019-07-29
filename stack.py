class Stack:
    start = 0
    rear = 0
    dic = {}

    def push(self, value):
        self.rear += 1
        self.dic[self.rear] = value
        return self.start, self.rear, self.dic, value

    def pop(self):
        popvalue = self.dic[self.rear]
        del self.dic[self.rear]
        self.rear -= 1
        return self.dic, popvalue

    def size(self):
        return self.dic, (self.rear - self.start)

# s = Stack()

# print(s.push(21))
# print(s.size())
# print(s.push(33333))
# print(s.size())
# print(s.push(45435))
# print(s.pop())
# print(s.size())

print("NEW SSSSSSSTACK()s for every single line")

print(Stack().push(21))
print(Stack().size())
print(Stack().push(33333))
print(Stack().size())
print(Stack().push(45435))
print(Stack().pop())
print(Stack().size())
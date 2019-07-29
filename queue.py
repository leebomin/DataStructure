class Queue:
    start = 0
    rear = 0
    dic = {}

    def enqueue(self, value):
        self.dic[self.rear] = value
        self.rear = self.rear + 1
        return self.start, self.rear, self.dic, value

    def dequeue(self):
        pop = self.dic[0]
        del self.dic[0]
        return pop

    def size(self):
        return len(self.dic)

q = Queue()

print(q.enqueue(324535))
print(q.size())
print(q.enqueue(321))
print(q.size())
print(q.dequeue())
print(q.size())

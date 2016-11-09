class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

x = Stack()

print(x.size())

#Using these processes on an empty stack will cause errors
"""#Popping an empty stack.
print(x.pop())
#Peeking at the top of a stack
print(x.peek())
"""
print("x.push('Rod')| Push Rod onto the stack :")
x.push("Rod")
#####
print("")
#####
print("x.push('Jane') | Push Jane onto the stack:")
x.push("Jane")
#####
print("")
#####
print("x.push('Freddy') | Push Freddy onto the stack:")
x.push("Freddy")
#####
print("")
#####
print("x.peek() | Peek at the top of the stack :")
print(x.peek())
#####
print("")
#####
print("x.pop() | Pop the last entity add to the stack LIFO :")
print(x.pop())
#####
print("")
#####
print("x.peek() | Peek at the top of the stack:")
print(x.peek())
#####
print("")
#####
print("x.size() | To get the size of the stack:")
print(x.size())

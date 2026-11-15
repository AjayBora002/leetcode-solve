class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return len(self.items) ==0

  def push(self, items):
    self.items.append(item)

  def pop(self):
    if len(self.items) == 0:
      return "Cannot pop"
    x = self.items.pop()
    return x

  def top(self):
    if len(self.items) == 0:
      return "Cannot top"
    return self.items[-1]

  def size(self):
    return len(self.items)


stack = Stack()
stack.push(8)
stack.pop()



class ArrayStack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.top = -1

    def push(self, x: int) -> None:
        if self.top == self.capacity - 1:
            raise OverflowError("Stack Overflow: Cannot push to a full stack")
        self.top += 1
        self.arr[self.top] = x

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot pop from an empty stack")
        val = self.arr[self.top]
        self.arr[self.top] = None  # Prevent memory leak
        self.top -= 1
        return val

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.arr[self.top]

    def is_empty(self) -> bool:
        return self.top == -1

    def size(self) -> int:
        return self.top + 1
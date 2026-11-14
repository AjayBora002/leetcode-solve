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

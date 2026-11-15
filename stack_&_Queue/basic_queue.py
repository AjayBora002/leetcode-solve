class Queue:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return len(self.items) == 0

  def enqueue(self, item):
    self.items.append(item)

  def dequeue(self):
    if len(self.items) == 0:
      print("empty")
      return 
    x = self.items.pop()
    return x

  def fromt(self):
    if len(self.items) == 0:
      print("cannot peek")
      return 
    return self.items[0]

  def rear(self):
    if len(self.items) ==0 :
      print("empty")
    return self.items[-1]

  def size(self):
    return len(self.items)
class CircularArrayQueue:
  def __init__(self, capacity:int):
    self.capacity = capacity
    self.arr = [None] * capacity
    self.front = -1
    self.rear = -1
    self.curr_size = 0

    def push(self, x):
      if self.curr_size == capacity:
        raise OverflowError("Queue Overflow")
      if self.curr_size ==0:
        self.front = 0
        self.rear = 0

      else:
        self.rear= (self.rear + 1) % self.capacity
        self.arr[self.rear] = x
        self.curr_size+=1


    def pop(self):
      if self.curr_Size ==0:
        raise IndexError("Queue underflow")
      val = self.arr[self.front]
      self.arr[self.front] = None
      if self.curr_size ==1:
        self.front = -1
        self.rear = -1
      else:
        self.front =(self.front +1) % self.capacity
      self.curr_size-=1
      return val
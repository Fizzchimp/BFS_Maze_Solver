class LQueue:
  
  def __init__(self, size):
    self.front = 0
    self.rear = -1
    self.size = size
    self.queue = [None for i in range(size)]
    
  def isFull(self):
    if self.rear == self.size - 1:
      return True
    return False
    
  def enqueue(self, item):
    if not self.isFull():
      self.rear += 1
      self.queue[self.rear] = item
    else: print("Queue is full.")

  def isEmpty(self):
    if self.front == self.rear + 1:
      return True
    return False
  
  def dequeue(self):
    if not self.isEmpty():
      self.queue[self.front] = None
      self.front += 1
    else: print("Queue is empty.")
      
  def display(self):
    print(self.queue)
    print(f"Front: {self.queue[self.front]}, Pos: {self.front}")
    print(f"Rear: {self.queue[self.rear]}, Pos: {self.rear}")
    
  def search(self, item):
    for i in range(self.front, self.rear + 1):
      if item.position == self.queue[i].position:
        return True
    return False   

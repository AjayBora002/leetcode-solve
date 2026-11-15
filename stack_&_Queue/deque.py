# Python provides deque in the collections module.

from collections import deque

q = deque()
# Enqueue
q.append(10)
q.append(20)
q.append(30)

# Dequeue
x = q.popleft()


# 2. Important deque operations
# Operation	Python method	Time Complexity
# Enqueue (rear)	q.append(x)	O(1)
# Dequeue (front)	q.popleft()	O(1)
# Front element	q[0]	O(1)
# Rear element	q[-1]	O(1)
# Queue size	len(q)	O(1)
# Check empty	not q	O(1)


# pop(0) takes O(n) time because remaining elements must shift.

# Instead, prefer:
from collections import deque
q = deque()

q.append(10)
q.popleft()




# 5. Bounded deque
# You can also specify a maximum capacity:

q = deque(maxlen=3)

q.append(10)
q.append(20)
q.append(30)
q.append(40)

print(q)
# deque([20, 30, 40], maxlen=3)
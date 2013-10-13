# example of queue
from collections import deque

queue = deque(['e1', 'e2', 3, 'e4'])
print queue

# add to the right
queue.append('e5')
# pop from the left
print queue.popleft()
print queue

for e in queue:
  print e
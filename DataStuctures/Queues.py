# follows FIFO model First in first out
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
# Removes the first item in the list
queue.popleft()
print(queue)
if not queue:
    print("empty")

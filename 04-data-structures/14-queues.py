from collections import deque

queue = deque([])
queue.append("send mail")
queue.append("copy file")
queue.append("make backup")
print(queue)
queue.popleft()
print(queue)

if not queue:
    print("empty")

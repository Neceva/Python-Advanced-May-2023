from collections import deque

text = deque(input().split())
text.reverse()

print(*text, sep=" ")
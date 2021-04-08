import collections
root = 3
tree = collections.defaultdict(list)
tree[3] = [9, 20]
tree[20] = [15,7]

q = collections.deque()
q.append((root, 1))
ans = 1
while q:
    val, depth = q.popleft()
    ans = depth

    if tree[val]:
        for i in tree[val]:
            q.append((i, depth+1))

print(ans)

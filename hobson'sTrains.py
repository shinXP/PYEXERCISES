import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    n, k = map(int, input[ptr:ptr+2])
    ptr += 2
    d = list(map(int, input[ptr:ptr+n]))
    ptr += n
    d = [x-1 for x in d]  # converting to 0-based index

    in_degree = [0] * n
    for i in range(n):
        in_degree[d[i]] += 1

    q = deque()
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)

    # Process the nodes in topological order
    # We'll mark nodes not in cycles and compute their depth from the cycle
    is_in_cycle = [True] * n
    depth = [0] * n
    while q:
        u = q.popleft()
        is_in_cycle[u] = False
        v = d[u]
        in_degree[v] -= 1
        if in_degree[v] == 0:
            q.append(v)
        depth[v] = depth[u] + 1

    # For nodes in cycles, find the cycle length and members
    visited = [False] * n
    res = [0] * n

    for u in range(n):
        if not visited[u] and is_in_cycle[u]:
            # Find the cycle
            cycle = []
            v = u
            while True:
                if visited[v]:
                    break
                visited[v] = True
                cycle.append(v)
                v = d[v]
            cycle_len = len(cycle)
            # For each node in the cycle, the answer includes min(k, cycle_len - 1) steps around the cycle plus the tree nodes
            for v in cycle:
                max_cycle_steps = min(k, cycle_len - 1)
                res[v] = max_cycle_steps + 1

    res = [0] * n
    reverse_graph = [[] for _ in range(n)]
    for i in range(n):
        reverse_graph[d[i]].append(i)

        for u in range(n):
            q = deque()
            q.append((u, 0))
            count = 0
            visited_bfs = [False] * n
            visited_bfs[u] = True
            while q:
                node, steps = q.popleft()
                if steps > k:
                    continue
                count += 1
                for neighbor in reverse_graph[node]:
                    if not visited_bfs[neighbor]:
                        visited_bfs[neighbor] = True
                        q.append((neighbor, steps + 1))
            res[u] = count

        print('\n'.join(map(str, res)))

    solve()
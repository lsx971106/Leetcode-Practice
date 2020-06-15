
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Solution 1: BFS

# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        queue = deque([node])
        clone_node = Node(node.val, [])
        visited = {node: clone_node}

        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])

        return visited[node]
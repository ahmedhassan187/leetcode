from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        colors = [0] * n  # 0: unvisited, 1: visiting, 2: visited
        safe_nodes = []

        def is_eventual_safe(node: int) -> bool:
            if colors[node] != 0:
                return colors[node] == 2

            colors[node] = 1  # Mark node as visiting
            
            for neighbor in graph[node]:
                if colors[neighbor] == 1 or not is_eventual_safe(neighbor):
                    return False

            colors[node] = 2  # Mark node as visited
            return True

        for node in range(n):
            if is_eventual_safe(node):
                safe_nodes.append(node)

        return safe_nodes

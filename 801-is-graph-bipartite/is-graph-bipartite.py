class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(node, clr):
            color[node] = clr

            for nei in graph[node]:
                if color[nei] == -1:
                    if not dfs(nei, 1 - clr):
                        return False
                elif color[nei] == clr:
                    return False

            return True

        for i in range(n):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False

        return True

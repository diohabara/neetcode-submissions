class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree なら edge 数は必ず n - 1
        # 多い: cycle がある
        # 少ない: disconnected
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)

        # undirected なので両方向
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            # connected check 用
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        # 0 から行けるノードを全部塗る
        dfs(0)

        # edge数が n-1 で、全部つながっていれば tree
        return len(visited) == n
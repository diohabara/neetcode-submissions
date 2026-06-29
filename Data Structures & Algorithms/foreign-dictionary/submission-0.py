class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegrees = {}
        for word in words:
            for ch in word:
                indegrees[ch] = 0
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for j in range(min(len(w1), len(w2))):
                c1 = w1[j]
                c2 = w2[j]
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegrees[c2] += 1
                    break
        q = deque()
        for ch in indegrees:
            if indegrees[ch] == 0:
                q.append(ch)
        res = []
        while q:
            ch = q.popleft()
            res.append(ch)

            for nei in graph[ch]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        if len(res) != len(indegrees):
            return ""
        return "".join(res)
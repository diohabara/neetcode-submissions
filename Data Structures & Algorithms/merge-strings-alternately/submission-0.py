class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        shorter, longer = min(len(word1), len(word2)), max(len(word1), len(word2))
        # append [0, shorter)
        for i in range(shorter):
            res.append(word1[i])
            res.append(word2[i])
        # append [shorter, longer)
        for j in range(shorter, longer):
            if len(word1) < len(word2):
                res.append(word2[j])
            else:
                res.append(word1[j])
        return "".join(res)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.word = word
        ROWS, COLS = len(board), len(board[0])
        res = []
        def dfs(r, c, node):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            ch = board[r][c]
            if ch == '#' or ch not in node.children:
                return
            child = node.children[ch]
            if child.word is not None:
                res.append(child.word)
                child.word = None
            board[r][c] = '#'
            dfs(r + 1, c, child)
            dfs(r - 1, c, child)
            dfs(r, c + 1, child)
            dfs(r, c - 1, child)
            board[r][c] = ch
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return res

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

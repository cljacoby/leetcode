# https://leetcode.com/problems/implement-trie-prefix-tree

class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.is_terminal = False
        self.children = dict()

class Trie(object):
    def __init__(self):
        self.root = TrieNode('') 

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        last = len(word) - 1
        for i, char in enumerate(word):
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
            if i == last:
                node.is_terminal = True
    
    def _find(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self._find(word)
        if node == None:
            return False
        return node.is_terminal
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self._find(prefix)
        if node == None:
            return False
        return True 

if __name__ == "__main__":
    trie = Trie()
    sequence = zip(
        ["insert",  "search",   "search",   "startsWith",   "insert",   "search"],
        ["apple",   "apple",    "app",      "app",          "app",      "app"],
        [None,      True,       False,      True,           None,       True],
    )
    for (method, arg, output) in sequence:
        result = getattr(trie, method)(arg)
        assert result == output, \
            f"result {result} != output {output} for method {method} arg {arg}"
    print("✅ All tests passed")


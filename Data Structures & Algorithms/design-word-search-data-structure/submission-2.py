class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.children = {}
        self.isEnd = False
 
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.isEnd = True

    def search(self, word: str, root=None) -> bool:
        """
        How to handle wildcards?
        
        If the current char is a wildcard, then have to check each child for the pattern
        "Does this child match rest, does this match rest, etc."
        recurse?

        if char == ".":
            # treat as new root? search for rest in all children?
            # but no, should be false because of length
            isIn = search(root=curr, word.slice(i))
            if isIn:
                return ?

        "b.y"
                *
        d       b       m
        a      a  u     a
        y      y  y     y
        """
        curr = root if root is not None else self.root
        for i, char in enumerate(word):
            # If wildcard, then we need to check each child for the presence of original word
            # Pass in the remaining suffix, assuming the wildcard is the child
            if char == ".":
                for childChar in curr.children:
                    child = curr.children[childChar]
                    if self.search(childChar + word[i + 1:], curr):
                        return True
                return False
            elif char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return curr.isEnd
        

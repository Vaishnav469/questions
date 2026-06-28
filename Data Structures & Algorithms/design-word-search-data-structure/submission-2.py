class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.endofword = True
        

    def search(self, word: str) -> bool:
        root = self.root
        def find(curr, word):
            if not word and curr.endofword:
                return True
            elif not word:
                return False
            elif word[0] != ".":
                if not (word[0] in curr.children):
                    return False
                else:
                    return find(curr.children[word[0]], word[1:])
            else:
                for value in curr.children.values():
                    if find(value, word[1:]):
                        return True
                    
                return False
            return False
        return find(root, word)
    
    
        

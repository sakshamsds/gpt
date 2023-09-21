class TrieNode:
    def __init__(self):
        self.children = dict()   # char, TrieNode pair

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]        
                

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True

    def startsWith(self, prefix: str) -> bool:
        pass

obj = Trie()
obj.insert('apple')        
print(obj.root.children)
print(obj.root.children['a'].children)
print(obj.root.children['a'].children['p'].children)
print(obj.root.children['a'].children['p'].children['p'].children)
print(obj.root.children['a'].children['p'].children['p'].children['l'].children)
print(obj.root.children['a'].children['p'].children['p'].children['l'].children['e'].children)
print(obj.search('app'))

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
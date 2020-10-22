class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.tree
        for a in word:
            if a not in node.keys():
                node[a] = {}
            node = node[a]
            print(self.tree)
        node["$"] = None
        print(self.tree)



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.tree
        for a in word:
            if a in node.keys():
                node = node[a]
            else:
                return False
        if "$" in node.keys():
            return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.tree
        for a in prefix:
            if a in node.keys():
                node = node[a]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
word="apple"
prefix="app3"
obj = Trie()
obj.insert(word)
print(obj.search(word))
print(obj.search(prefix))
print(obj.startsWith(prefix))

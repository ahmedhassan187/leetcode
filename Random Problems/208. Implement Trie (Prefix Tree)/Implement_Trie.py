class Trie:
    list_of_hash = []
    strings = []
    def __init__(self):
        Trie.strings = []
        Trie.list_of_hash = []
        for i in range(20):
            Trie.list_of_hash.append([])
    def insert(self, word: str) -> None:
        result = (hash(word)%20)
        Trie.list_of_hash[result].append(word)
        Trie.strings.append(word)
    def search(self, word: str) -> bool:
        result = (hash(word)%20)
        for i in range(len(Trie.list_of_hash[result])):
            if Trie.list_of_hash[result][i] == word:
                return True
        return False
    def startsWith(self, prefix: str) -> bool:
        for i in range(len(Trie.strings)):
            counter = 0
            for j in range(len(prefix)):
                if len(prefix) > len(Trie.strings[i]):
                    break
                if prefix[j] == Trie.strings[i][j]:
                    counter +=1
                else:
                    counter = 0
                    break
            if counter !=0:
                return True
        return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

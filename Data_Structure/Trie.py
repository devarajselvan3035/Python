"""
TrieNode
Args:
1. Children: Each TrieNode has a datastructure to store reference to its child nodes.
A hash map is typically used for this, with a character as the key and its
corresponding child node as the value.
2. **End of word indicator**: Each TrieNode needs an attribute to indicate whether it marks the end of a word. This can be done in two ways:
        - A boolean attribute (is_word) to confirm if the node is the end of a word
        - A string variable (word) that stores the word itself at the node. This is usually used if we also want to know the specific word that ends at this node.
"""


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word: str) -> None:
        curdNode = self.root
        for chr in word:
            if chr not in curdNode.children:
                curdNode.children[chr] = TrieNode()
            curdNode = curdNode.children[chr]
        curdNode.isWord = True

    def search(self, word) -> bool:
        curdNode = self.root
        for chr in word:
            if chr not in curdNode.children:
                return False
            curdNode = curdNode.children[chr]
        return curdNode.isWord

    def delete(self, word) -> None:
        pass

    def show(self) -> None:
        curdNode = self.root
        while not curdNode.isWord:
            pairs = list(curdNode.children.items())
            print(pairs[0][0])
            curdNode = pairs[0][1]

    def _delete(self, word, curdNode):
        if len(word) == 0:
            return None
        self._delete(word[1:], curdNode.children[word[0]])


if __name__ == "__main__":
    trie = Trie()
    trie.add("good")
    trie.add("go")
    trie.show()
    print(trie.search("go"))

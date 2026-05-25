class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
            
        curr.is_word = True
        
    def contains_word(self, word):
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                return False

            curr = curr.children[char]
        
        return curr.is_word
    
    def contains_prefix(self, prefix):
        curr = self.root
        
        for char in prefix:
            if char not in curr.children:
                return False

            curr = curr.children[char]
            
        return True
   
def load_words(filename):
    with open(filename, "r") as file:
        text = file.read()
    
    words = text.split()
    return words
    
    
    
def main():
    
    # open the file 
    words = load_words("eng2000.txt")
    
    # sort the file into a trie 
    trie = Trie()
    
    for word in words:
        trie.insert(word.lower())
        
    # testing the trie
    print("Total words loaded:", len(words))
    print(trie.contains_word("apple"))
    print(trie.contains_prefix("app"))
    print(trie.contains_word("zzzz"))
    
    test_word = words[0].lower()
    print(test_word + ":", trie.contains_word(test_word))
    
    

# import game state (matrix?), can be hard coded for now 

# implement algorithm, print possible words
    
main()









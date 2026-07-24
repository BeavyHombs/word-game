MIN_WORD_LENGTH = 3

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
            # if prefix doesn't exist already
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
    words = load_words("google-10000-english.txt")
    
    # sort the file into a trie 
    trie = Trie()
    
    for word in words:
        trie.insert(word.lower())
        
    # # testing the trie
    # print("Total words loaded:", len(words))
    # print(trie.contains_word("apple"))
    # print(trie.contains_prefix("app"))
    # print(trie.contains_word("zzzz"))
    
    # test_word = words[0].lower()
    # print(test_word + ":", trie.contains_word(test_word))
 
    # more testing 
    possible_words = find_words(board, trie)
    print('Possible words: ', len(possible_words))
    print(sorted(possible_words))   
    

# import game state (matrix?), can be hard coded for now 

board = [
    ["o", "a", "t", "r"],
    ["i", "h", "p", "s"],
    ["h", "t", "n", "r"],
    ["e", "n", "e", "i"]
]

# implement algorithm, print possible words

def find_words(board, trie):
    found = set()
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            search(board, r, c, trie.root, "", set(), found)
            
    return found

def search(board, r, c, node, current_word, visited, found):
    """Recursive search that takes in: 
        board: the game board.
        r: the row coordinate. 
        c: the column coordinate.
        node: the Trie node representing current_word before this cell is consumed
        current_word: the word/prefix that has been traversed through so far.
        visited: coordinates used in current path.
        found: a set of words that have been found. 
    """
    # already seen or out of bounds
    position = (r, c)
    if position in visited or not (0 <= r < len(board) and 0 <= c < len(board[0])):
        return 
    
    # read the letter
    letter = board[r][c]
    
    # check whether letter is a child of current node
    if letter in node.children:
        node = node.children[letter]
        current_word += letter
    else: 
        return

    # check if newly created prefix is a word AND only include the word if of sufficent length according to GP rules
    if node.is_word and len(current_word) >= MIN_WORD_LENGTH:
        found.add(current_word)
    
    # current position is now visited
    visited.add(position)
    
    # check each neighbor recursively (ordered like a numeric pad)
    search(board, r - 1, c - 1, node, current_word, visited, found)
    search(board, r, c - 1, node, current_word, visited, found)
    search(board, r + 1, c - 1, node, current_word, visited, found)
    search(board, r - 1, c, node, current_word, visited, found)
    search(board, r + 1, c, node, current_word, visited, found)
    search(board, r - 1, c + 1, node, current_word, visited, found)
    search(board, r, c + 1, node, current_word, visited, found)
    search(board, r + 1, c + 1, node, current_word, visited, found)
    
    # remove position from visited (to allow for backtracking)
    visited.remove(position)
    
main()










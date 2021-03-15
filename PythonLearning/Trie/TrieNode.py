class TrieNode:
    def __init__(self,char=''):
        self.children = [None]*26
        self.is_end_word = False
        self.character = char

    def set_end_word(self):
        self.is_end_word=True

    def reset_end_word(self):
        self.is_end_word=False
        
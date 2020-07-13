class Solution(object):
    def detectCapitalUse(self, word):
        if word[0].islower():
            if word == word.lower():
                return True
            return False
        if word[0].isupper():
            if word==word.upper():
                return True
            elif word[1:]==word[1:].lower():
                return True
            else:
                return False
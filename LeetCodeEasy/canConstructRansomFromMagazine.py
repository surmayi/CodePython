class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine=list(magazine)
        for ch in ransomNote:
            if ch in magazine:
                magazine.remove(ch)
            else:
                return False
        return True
        
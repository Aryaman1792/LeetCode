class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in word and ch.upper() in word:
                if word.rfind(ch)<word.find(ch.upper()):
                    count+=1
        return count
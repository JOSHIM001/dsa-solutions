class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        freq={}
        words=s.split(" ")
        if len(words)!=len(pattern):
            return False
        for i in range(len(pattern)):
            p=pattern[i]
            word=words[i]
            if p in freq:
                 if freq[p]!=word:
                    return False
            else:
                if word in freq.values():
                    return False
            freq[p]=word
        return True


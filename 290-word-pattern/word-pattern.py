class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s=s.split()
        h1={}
        h2={}
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] in h1 and h1[pattern[i]]!=s[i]:
                return False
            if s[i] in h2 and h2[s[i]]!=pattern[i]:
                return False
            h1[pattern[i]]=s[i]
            h2[s[i]]=pattern[i]
        return True

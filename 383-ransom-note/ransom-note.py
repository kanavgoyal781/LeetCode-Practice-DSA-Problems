class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h1={}
        h2={}
        for i in ransomNote:
            if i in h1:
                h1[i]=h1[i]+1
            else:
                h1[i]=1
        for j in magazine:
            if j in h2:
                h2[j]=h2[j]+1
            else:
                h2[j]=1
        for key,values in h1.items():
            if key not in h2.keys():
                return False
            if h2[key]<values:
                return False
        return True

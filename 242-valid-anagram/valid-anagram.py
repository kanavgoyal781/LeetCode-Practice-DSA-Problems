class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm={}
        hm2={}
        for i in s:
            if i in hm:
                hm[i]=hm[i]+1
            else:
                hm[i]=1
        for j in t:
            if j in hm2:
                hm2[j]=hm2[j]+1
            else:
                hm2[j]=1
        return hm==hm2
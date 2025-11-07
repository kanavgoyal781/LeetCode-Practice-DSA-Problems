class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm_s={}
        hm_t={}
        for i in s:
            if i in hm_s.keys():
                hm_s[i]=hm_s[i]+1
            else:
                hm_s[i]=1
        for j in t:
            if j in hm_t.keys():
                hm_t[j]=hm_t[j]+1
            else:
                hm_t[j]=1
        print(hm_s)
        print(hm_t)
        return hm_s==hm_t
        
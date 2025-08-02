class Solution:
    def intToRoman(self, num: int) -> str:
        ans=""
        h={}
        h["M"]=1000
        h["CM"]=900
        h["D"]=500
        h['CD']=400
        h['C']=100
        h['XC']=90
        h["L"]=50
        h['XL']=40
        h["X"]=10
        h['IX']=9
        h["V"]=5
        h['IV']=4
        h['I']=1
        # val=1000
        for symbol, value in h.items():
            c=num//value
            ans=ans+symbol*c
            num=num%value
        return ans

            

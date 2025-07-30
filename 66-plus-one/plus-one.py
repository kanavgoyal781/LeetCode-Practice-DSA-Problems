class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig_str=""
        num=[]
        for i in digits:
            dig_str=dig_str+str(i)
        # print(int(dig_str))
        final_dig_str=str(int(dig_str)+1)
        for i in final_dig_str:
            num.append(int(i))
        return num
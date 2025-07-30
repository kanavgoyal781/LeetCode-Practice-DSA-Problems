class Solution:
    def trailingZeroes(self, n: int) -> int:
        num=1
        count=0
        if n==0:
            return 0
        k=5
        while k<=n:
            count=floor(n/k)+count
            k=k*5
        return int(count)
        
        
        # for i in range(n,1,-1):
        #     num=num*i
        # print(num)
        # while num%10==0:
        #     num=int(num/10)
        #     count=count+1
        #     print(num)
        # return count
        # # num_str=str(num)
        # # right=len(num_str)-1
        # # for i in range(len(num_str)):
        # #     if num_str[right-i]=="0":
        # #         count=count+1
        # #     else:
        # #         break
        # # return count


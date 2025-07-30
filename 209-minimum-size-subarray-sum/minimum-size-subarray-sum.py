class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        sum=nums[left]
        if nums[0]>target:
            return 1
        length=float("inf")
        ans=False
        for i in nums:
            if i>=target:
                return 1
        while right<len(nums):
            if sum<target:
                right=right+1
                if right == len(nums):
                    break
                sum=sum+nums[right]
                print(sum)
            else:
                length=min(length, right-left+1)
                sum=sum-nums[left]
                print(sum)
                left=left+1
                ans=True
        if ans==False:
            return 0
        else:
            return length
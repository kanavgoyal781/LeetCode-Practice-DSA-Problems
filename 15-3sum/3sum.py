class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        temp=set()
        nums.sort()
        for i in range(len(nums)):
            left=i+1
            right = len(nums)-1
            while left< right:
                if nums[i]+nums[left]+nums[right]==0:
                    temp.add((nums[i],nums[left],nums[right]))
                    left=left+1
                    right=right-1
                elif nums[i]+nums[left]+nums[right]>0:
                    right=right-1
                else:
                    left=left+1
        return [list(element) for element in temp]

            
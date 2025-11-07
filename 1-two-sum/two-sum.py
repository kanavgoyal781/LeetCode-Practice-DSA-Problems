class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for ind, val in enumerate(nums):
            if target-val in hm.keys():
                return [ind, hm[target-val]]
            hm[val]=ind
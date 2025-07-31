class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        point=0
        solution=[]
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [str(nums[0])]
        start=nums[0]
        while point<len(nums):
            if nums[point+1]-nums[point]==1:
                point=point+1
            else:
                if start==nums[point]:
                    solution.append(str(start))
                else: 
                    solution.append(str(start)+"->"+str(nums[point]))
                point=point+1
                start=nums[point]
            if point==len(nums)-1:
                break

        if start == nums[point]:
            solution.append(str(start))
        else:
            solution.append(f"{start}->{nums[point]}")
        return solution

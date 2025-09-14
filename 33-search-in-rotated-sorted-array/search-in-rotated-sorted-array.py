class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while(l<=r):
            mid=int((l+r)/2)
            if target==nums[mid]:
                return mid
            elif nums[l]<nums[mid]:
                if mid >0 and nums[l]<=target<=nums[mid-1]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if mid <len(nums)-1 and nums[mid+1]<=target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1


                #now we will search in the right

        #     if r<len(nums)-1 and nums[mid]>target and nums[mid+1]>nums[mid]:
        #         end=mid-1
        #     elif r<len(nums)-1 and nums[mid]>target and nums[mid+1]<nums[mid]:
        #         start=mid+1
        #     elif r<len(nums)-1 and nums[mid]<target and nums[mid+1]>nums[mid]:
        #         start=mid+1
        #     elif r<len(nums)-1 and nums[mid]<target and nums[mid+1]<nums[mid]:
        #         end=mid-1
        #     else:
        #         return mid
        # return -1
            
            
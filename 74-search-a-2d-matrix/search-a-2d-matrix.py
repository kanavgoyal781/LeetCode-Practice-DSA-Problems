class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        row_to_check=-1
        start=0
        end=rows-1
        while start<=end:
            mid=int(start+(end-start)/2)
            if matrix[mid][0]<=target and target<=matrix[mid][cols-1]:
                row_to_check=mid
                break
            elif matrix[mid][0]>target:
                end=mid-1
            else:
                start=mid+1
        if row_to_check==-1:
            return False
        start=0
        end=cols-1
        while start<=end:
            mid=int(start+(end-start)/2)
            if matrix[row_to_check][mid]>target:
                end=mid-1
            elif matrix[row_to_check][mid]<target:
                start=mid+1
            else:
                return True
        return False
        
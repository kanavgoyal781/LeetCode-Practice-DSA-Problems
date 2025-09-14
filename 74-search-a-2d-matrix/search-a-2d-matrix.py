class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        row_to_check=0
        for i in range((rows)):
            if target>=matrix[i][0] and target<=matrix[i][cols-1]:
                row_to_check=i
        start=0
        end=cols-1
        for i in range(cols):
            mid=int(start+(end-start)/2)
            if matrix[row_to_check][mid]>target:
                end=mid-1
            elif matrix[row_to_check][mid]<target:
                start=mid+1
            else:
                return True
        return False
        
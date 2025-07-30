class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        cord=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    cord.append([i,j])
        if len(cord)==0:
            return matrix
        else:
            for element in cord:
                for row in range(m):
                    matrix[row][element[1]]=0
                for col in range(n):
                    matrix[element[0]][col]=0
        return matrix
        
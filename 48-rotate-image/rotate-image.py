class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length=len(matrix)
        for i in range(length-1):
            for j in range(i+1,length):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
        print(matrix)
        for i in range(length):
            for j in range(length//2):
                temp=matrix[i][j]
                matrix[i][j]=matrix[i][length-j-1]
                matrix[i][length-j-1]=temp
        return matrix



        
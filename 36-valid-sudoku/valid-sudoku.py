class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=[]
        unique=True
        for sublist in board:
            seen=[]
            for i in range(len(sublist)):
                if (sublist[i] not in seen) and (sublist[i].isnumeric()):
                    seen.append(sublist[i])
                elif (sublist[i] in seen) and (sublist[i].isnumeric()):
                    return False 
        for i in range(9):
            seen=[]
            for sub in board:
                if (sub[i] not in seen) and (sub[i].isnumeric()):
                    seen.append(sub[i])
                elif (sub[i] in seen) and (sub[i].isnumeric()):
                    return False
        
        for rows in range(0,9,3):
            for cols in range(0,9,3):
                seen=[]
                for i in range(3):
                    for j in range(3):
                        if board[rows+i][cols+j].isnumeric() and board[rows+i][cols+j] not in seen:
                            seen.append(board[rows+i][cols+j])
                        elif (board[rows+i][cols+j] in seen) and (board[rows+i][cols+j].isnumeric()):
                            return False
        return True

                    
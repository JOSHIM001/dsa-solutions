class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        empty=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    empty.append((i,j))
                else:
                    num=board[i][j]
                    box=(i//3)*3+(j//3)
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box].add(num)
        def back(idx):
            if idx==len(empty):
                return True
            row,col=empty[idx]
            box=(row//3)*3+(col//3)
            for num in '123456789':
                if num not in rows[row] and num not in cols[col] and num not in boxes[box]:
                    board[row][col]=num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box].add(num)
                    if back(idx+1):
                        return True
                    board[row][col]="."
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box].remove(num)
            return False
        back(0)
                    

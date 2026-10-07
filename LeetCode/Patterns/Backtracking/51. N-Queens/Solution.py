class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        cols=set()
        dig1=set()
        dig2=set()
        board=[['.']*n for _ in range(n)]
        def back(row):
            if row==n:
                res.append([''.join(r) for r in board])
                return 
            for col in range(n):
                if col in cols or (row-col) in dig1 or (row+col) in dig2:
                    continue
                board[row][col]='Q'
                cols.add(col)
                dig1.add(row-col)
                dig2.add(row+col)
                back(row+1)
                board[row][col]='.'
                cols.remove(col)
                dig1.remove(row-col)
                dig2.remove(row+col)
        back(0)
        return res

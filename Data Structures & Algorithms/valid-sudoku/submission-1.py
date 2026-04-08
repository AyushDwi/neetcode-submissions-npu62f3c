class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(0,9):
            hashset_row=set()
            for j in range(0,9):
                if board[i][j]==".":
                    continue
                if board[i][j] in hashset_row:
                    return False
                hashset_row.add(board[i][j])

        for i in range(0,9):
            hashset_col=set()
            for j in range(0,9):
                if board[j][i]==".":
                    continue
                if board[j][i] in hashset_col:
                    return False
                hashset_col.add(board[j][i])   
        
        hashmap_sq=collections.defaultdict(set)

        for r in range(0,9):
            for c in range(0,9):
                if board[r][c]==".":
                    continue
                if board[r][c] in hashmap_sq[(r//3,c//3)]:
                    return False
                hashmap_sq[(r//3,c//3)].add(board[r][c])

        return True                
                            
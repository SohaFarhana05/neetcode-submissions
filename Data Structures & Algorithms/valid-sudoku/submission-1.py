class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidRow(row):
            arr = [0]*10
            for i in range(len(row)):
                if row[i]=='.':
                    continue
                elif arr[int(row[i])]==1:
                    return False
                else:
                    arr[int(row[i])]=1
            return True 
        def isValidCol(col):
            arr = [0]*10
            for i in range(len(col)):
                if col[i]=='.':
                    continue
                elif arr[int(col[i])]==1:
                    return False
                else:
                    arr[int(col[i])]=1
            return True 
        
        for i in range(len(board)):
            # print(board[i])
            if isValidRow(board[i]):
                continue
            else:
                return False
        j=0
        i=0
        arr = []
        while j<len(board[0]):
            while i<len(board):
                arr.append(board[i][j])
                i+=1
            if not isValidCol(arr):
                return False
            # else:
            #     return False
            arr = []
            i=0
            j+=1
            
            
        def valid(arr):
            s=set()
            for i in arr:
                if i=='.':
                    continue
                if i in s:
                    return False
                else:
                    s.add(i)
            return True

        for r in range(0,len(board),3):
            for c in range(0,len(board[0]),3):
                box = []
                for i in range(r,r+3):
                    for j in range(c,c+3):
                        box.append(board[i][j])
                if not valid(box):
                    return False




        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [{},{},{},{},{},{},{},{},{}]
        rows = []
        squares = [ [{},{},{}], [{},{},{}] , [{},{},{}] ]

        for i in range(len(board)):
            r = {}
            row = board[i]

            for j in range(len(row)):
                char = row[j]

                sq = squares[int(i/3)]
                s = sq[int(j/3)]
                if char != ".":
                    if char in s:
                        return False
                    else:
                        s[char] = 1


                c = columns[j]
                if char != ".":
                    if char in c:
                        return False
                    else:
                        c[char] = 1

                if char != ".":
                    if char in r:
                        return False
                    else:
                        r[char] = 1
        
        
        return True
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        if numRows==1:
            return s
        numCols = int(length/(numRows-1))+1
        print('numCols={}'.format(numCols))
        m = [['' for i in range(numCols)] for j in range(numRows)]
        i = 0
        col = 0
        row = 0
        while i < length:
            
            while row<numRows and i < length:
                m[row][col]=s[i]
                i = i+1
                row = row+1
            col = col+1
            row = numRows-2
            #print(m)
            while row>=0 and i < length:
                #print("row={}, col={}, i = {}".format(row, col, i))
                m[row][col] = s[i]
                i=i+1
                row = row-1
            col = col+1
            row = 1
            #print(m)
        res = ''
        for row in range(numRows):
            for col in range(numCols):
                res = res+m[row][col]
        return res
            


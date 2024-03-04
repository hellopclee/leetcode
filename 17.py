class Solution:
    num_letter = ['','', 'abc', 'def','ghi','jkl', 'mno','pqrs','tuv','wxyz']

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        return self.trans(digits)


    def trans(self, digits):
        size = len(digits)
        if size==1:
            return list(self.num_letter[int(digits)])
        else:
            res =[]
            #print(size)
            letters = self.trans(digits[size-1])
            i = len(letters)
            for j in self.trans(digits[0:size-1]):
                for k in letters:
                    res.append(j+k)
            return res


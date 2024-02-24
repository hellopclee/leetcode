class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chset = set()
        length = len(s)
        maxsize = 0
        head = 0
        tail = 0
        while tail < length:
            if s[tail] not in chset:
                chset.add(s[tail])
                tail=tail+1
                tmp = tail-head
                if tmp>maxsize:
                    maxsize = tmp
                continue
            else:
                tmp = tail-head
                if tmp>maxsize:
                    maxsize = tmp
                while s[head]!=s[tail]:
                    chset.remove(s[head])
                    head = head+1
                chset.remove(s[head])    
                head = head +1
                chset.add(s[tail])
                tail = tail+1


        return maxsize


#42:34
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)

        if size == 1:
            return s[0]
        elif size == 2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]
        else:
            max_ps = 1
            i = 0
            pstring = s[0]

            while i < size:
                current_ps = 1
                cstring = s[i]
                # 第一种情况 aba
                j=1
                while (i+j)<size and (i-j)>= 0 and s[i+j]==s[i-j]:
                    current_ps = current_ps+2
                    cstring = s[i-j]+cstring+s[i+j]
                    j=j+1
                if current_ps>max_ps:
                    max_ps = current_ps
                    pstring = cstring
                #第二种情况xxaaxx
                if i+1<size and s[i]==s[i+1]:
                    current_ps=2
                    cstring = s[i]+s[i+1]
                    j=1
                    while (i+1+j)<size and (i-j)>=0 and s[i-j]==s[i+1+j]:
                        current_ps = current_ps+2
                        cstring = s[i-j]+cstring+s[i+1+j]
                        j=j+1
                    if current_ps>max_ps:
                        max_ps = current_ps
                        pstring = cstring

                i=i+1
            
            return pstring
             



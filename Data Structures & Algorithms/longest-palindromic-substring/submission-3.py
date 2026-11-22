class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = (0,0)
        if len(s) == 1:
            return s[0]

        for i in range(0,len(s)):
            
            #handle odd case
            l, r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > (longest[1] - longest[0] + 1):
                    longest = (l,r)  
                l -= 1
                r += 1
            l, r = i, i+1
            #handle even case
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > (longest[1] - longest[0] + 1):
                    longest = (l,r)  
                l -= 1
                r += 1
        return s[longest[0]:longest[1]+1]

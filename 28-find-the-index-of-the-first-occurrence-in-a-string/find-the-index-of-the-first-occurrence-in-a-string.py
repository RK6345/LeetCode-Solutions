class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)):
            if haystack[i:len(needle)+i]==needle:
                return i
                    
        else:
            return -1
                
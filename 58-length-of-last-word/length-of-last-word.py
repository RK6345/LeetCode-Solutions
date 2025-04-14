class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.split()
        x=len(l)-1
        for i in range(len(l)):
            if l[x].isalpha():
                return len(l[x])
            x-=1    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x=(strs[0])

        for i in strs:
            if len(i)<len(x):
                x=i

        for i in strs:
            if x!=i[0:len(x)]:
                while len(x)<=len(i):
                    if x!=i[0:len(x)]:
                        x=x[0:len(x)-1]
                    else:
                        break  

        return x
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[]
        for i in range(numRows):
            t=[]
            for j in range(i+1):
                if  j==0 or j==i:
                    t.append(1)
                else:
                    x=l[i-1][j] + l[i-1][j-1]
                    t.append(x)
            l.append(t)
            
        return l 
  
  
        
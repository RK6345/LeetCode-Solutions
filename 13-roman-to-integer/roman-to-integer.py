class Solution:
    def romanToInt(self, s: str) -> int:
        n = 0
        d={"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, 
        "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}

        for i in range(len(s)):
            if i+1 < len(s) and d[s[i]] < d[s[i+1]]:
                n-=d[s[i]]

            else:
                n+=d[s[i]] 
        return n        
      
        
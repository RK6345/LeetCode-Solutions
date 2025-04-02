class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev, org = 0, x
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        
        return org == rev      
        
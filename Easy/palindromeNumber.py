class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        a_reversed = a[::-1]
        if(a == a_reversed):
            return True
        else:
            return False
        

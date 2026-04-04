class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        #s = s.split()
        s = ''.join(filter(str.isalnum, s))
        print(s)
        if s == s[::-1]:  
            return True
        else:
            return False
            
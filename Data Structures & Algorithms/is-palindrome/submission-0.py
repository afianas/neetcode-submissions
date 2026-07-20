class Solution:
    def isPalindrome(self, s: str) -> bool:
        stri=""
        for char in s:
            if char.isalnum():
                stri+=char
        stri=stri.lower()
        if stri==stri[::-1]:
            return True
        return False
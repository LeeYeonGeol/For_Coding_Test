class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        for i in s:
            if i.isdigit():
                s2 += i
            elif i.isalpha():
                s2 += i.lower()

        for i in range(len(s2)//2):
            if s2[i]  != s2[-1-i]:
                return False
        else:
            return True
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_l = 0
        substring = []
        sub = ""
        for i in range(len(s)):
            substring = s[i:]
            for j in range(len(s), i-1, -1):
                #if i!=j:
                substring = s[i:j]
                #else:
                    #substring = s[i]
                if judgePalindrome(substring):
                    if max_l < len(substring):
                        max_l = len(substring)
                        sub = substring
                        break
        return sub
                
def judgePalindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i = i+1
            j = j-1
        else:
            return False
    return True


s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("a"))
print(s.longestPalindrome("bb"))
print(s.longestPalindrome("ccc"))

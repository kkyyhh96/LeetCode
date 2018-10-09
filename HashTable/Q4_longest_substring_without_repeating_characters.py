class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = set()
        max_l = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                tmp_l = len(substring)
                substring.add(s[j])
                if len(substring) == tmp_l:
                    if max_l < tmp_l:
                        max_l = tmp_l
                    substring = set()
                    break
                else:
                    if max_l < len(substring):
                        max_l = len(substring)
        return max_l


        
s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))
print(s.lengthOfLongestSubstring('bbbb'))
print(s.lengthOfLongestSubstring('pwwkew'))
print(s.lengthOfLongestSubstring('a'))
print(s.lengthOfLongestSubstring(''))
print(s.lengthOfLongestSubstring('au'))
print(s.lengthOfLongestSubstring('dvdf'))

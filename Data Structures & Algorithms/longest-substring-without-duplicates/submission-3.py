class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        left = 0
        right = 0
        substring_set = set()
        length = 0

        while right < len(s):
            
            if s[right] not in substring_set:
                substring_set.add(s[right])
                right += 1
            else:
                while s[right] in substring_set:
                    substring_set.remove(s[left])
                    left += 1
                substring_set.add(s[right])
                right += 1

            length = max(length, len(substring_set))
        return length



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k > (len(s)-1):
            return k

        counter = {}
        left = 0
        right = 0
        max_freq = 0
        longest_substring = 0

        while right < len(s):
            # add s[right] to the window
            counter[s[right]] = counter.get(s[right], 0) + 1
            
            # update the max freq
            max_freq = max(max_freq, counter[s[right]])

            # check if window is too large, and not enough replacements available
            window_size = right - left + 1
            if window_size - max_freq > k:
                counter[s[left]] -= 1
                left += 1
            
            # update substring size
            longest_substring = max(longest_substring, right - left + 1)

            # move the right pointer
            right += 1
        
        return longest_substring
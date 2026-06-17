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
            
            max_freq = max(max_freq, counter[s[right]])

            window_size = right - left + 1
            if window_size - max_freq > k:
                counter[s[left]] -= 1
                left += 1
            
            longest_substring = max(longest_substring, right - left + 1)

            right += 1
        
        return longest_substring
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        possible_starts = []

        for num in nums:
            if num - 1 not in s:
                possible_starts.append(num)
        
        longest = 0
        for start in possible_starts:
            curr_seq = 1
            while start + (curr_seq-1) + 1 in s:
                curr_seq += 1
            longest = max(longest, curr_seq)

        return longest

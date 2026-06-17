class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()  # stores indices, values are kept in decreasing order

        for right in range(len(nums)):
            # Remove indices that are outside the current window
            # Current window is [right - k + 1, right]
            while q and q[0] <= right - k:
                q.popleft()

            # Remove smaller values from the back
            # They can never be the max while nums[right] is in the window
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # Add current index
            q.append(right)

            # Start recording answers once the first full window is formed
            if right >= k - 1:
                result.append(nums[q[0]])

        return result
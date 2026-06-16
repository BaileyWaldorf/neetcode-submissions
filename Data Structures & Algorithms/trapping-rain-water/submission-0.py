class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        rain_water = 0

        while left < right:
            if height[left] <= height[right]:
                # process left side
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # water can sit here
                    rain_water += left_max - height[left]
                left += 1
            elif height[right] < height[left]:
                # process right side
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    # water can sit here
                    rain_water += right_max - height[right]
                right -= 1
        
        return rain_water
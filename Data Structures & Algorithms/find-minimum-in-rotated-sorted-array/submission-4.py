class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) -1
        
        while left < right:
            mid = (right + left) // 2
            # print(mid)

            # if nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
            #     return nums[mid]
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = nums[0]
        found_zero = None

        for i in range(1, len(nums)):
            if nums[i] == 0 and not found_zero:
                found_zero = i
                continue
            product *= nums[i]
        
        if found_zero:
            return [0 if nums[i] != 0 else product for i in range(len(nums))]

        output = []

        for i, num in enumerate(nums):
            if num != 0:
                output.append(product // num)
        
        return output
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            result = self.twoSum(nums, i)
            if result:
                triplets.extend(result)
        
        return triplets
        
    def twoSum(self, nums: List[int], fixed_index: int) -> List[List[int]] | None:
        left = fixed_index + 1
        right = len(nums) - 1
        valid_triplets = []

        while left < right:
                total = nums[fixed_index] + nums[left] + nums[right]

                if total == 0:
                    valid_triplets.append([nums[fixed_index], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return valid_triplets
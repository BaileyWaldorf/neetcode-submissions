class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()


        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in map:
                return [map[compliment], i]
            else:
                map[nums[i]] = i
            
            print(map)

        return []
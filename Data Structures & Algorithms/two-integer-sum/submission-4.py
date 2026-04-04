class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map_val = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in map_val:
                return [map_val[diff], i]
            
            map_val[nums[i]] = i
           

            
        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        map_set = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]

            if diff in map_set:
                return [map_set[diff], i+1]
            
            map_set[numbers[i]] = i+1
                


        
        

        
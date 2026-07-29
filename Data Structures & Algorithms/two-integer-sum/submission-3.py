class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,e in enumerate(nums):
            difference=target-e
            if difference in hashmap:
                return [hashmap[difference],i]
            hashmap[e]=i



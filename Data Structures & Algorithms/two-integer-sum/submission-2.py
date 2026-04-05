class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]]=[i]
            elif nums[i] in hashmap:
                hashmap[nums[i]]+=[i]

        for i in range(len(nums)):
            difference=target-nums[i]            
            if difference in hashmap:
                for j in hashmap[difference]:
                    if j!=i:
                        return [i,j]
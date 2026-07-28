class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for i,e in enumerate(nums):
            if e not in hashset:
                hashset.add(e)
            elif e in hashset:
                return True
        return False            
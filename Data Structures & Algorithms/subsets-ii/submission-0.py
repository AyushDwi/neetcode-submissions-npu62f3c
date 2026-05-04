class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        subset=[]
        def dfs(start):
            if start>=(len(nums)):
                res.append(subset.copy())
                return
            #accept
            subset.append(nums[start])
            dfs(start+1)
            subset.pop()
            #reject
            while start+1<len(nums) and nums[start]==nums[start+1]:
                start+=1
            dfs(start+1)
        dfs(0)
        return res            
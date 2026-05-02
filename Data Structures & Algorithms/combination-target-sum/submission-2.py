class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        nums.sort()
        def dfs(start,sum_=0):
            if sum_>target:
                return
            if sum_==target:
                res.append(subset.copy())
                return
            if start<len(nums):
                #accept nums[start], then run dfs
                subset.append(nums[start])
                dfs(start,sum_+nums[start])
                #reject nums[start], then run dfs
                subset.pop()
                dfs(start+1,sum_)
                       
        dfs(start=0,sum_=0)
        return res                
from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(start: int, sum_: int):
            if sum_ == target:
                res.append(subset.copy())
                return
            if sum_ > target:
                return

            for i in range(start, len(nums)):
                # Optional pruning: if nums are sorted
                if sum_ + nums[i] > target:
                    break

                subset.append(nums[i])
                # i, not i+1, because we can reuse nums[i]
                dfs(i, sum_ + nums[i])
                subset.pop()

        dfs(0, 0)
        return res
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(0,len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
                
            target=-nums[i]
            j=i+1
            k=len(nums)-1

            while j<k:
                if nums[j]+nums[k]==target:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                if nums[j]+nums[k]>target:
                    k-=1
                    continue
                if nums[j]+nums[k]<target:
                    j+=1
                    continue
        return res                    

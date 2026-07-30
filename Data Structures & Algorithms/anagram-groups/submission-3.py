class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i,e in enumerate(strs):
            count=[0]*26
            for c in e:
                count[ord(c)-ord('a')]+=1
            res[tuple(count)].append(e) 
        ans=[]       
        for e in res:
            ans.append(res[e])
        return ans    
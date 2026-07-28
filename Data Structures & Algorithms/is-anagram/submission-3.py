class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1={}
        hashmap2={}

        for i,e in enumerate(s):
            if e not in hashmap1:
                hashmap1[e]=1
            elif e in hashmap1:
                hashmap1[e]+=1

        for i,e in enumerate(t):
            if e not in hashmap2:
                hashmap2[e]=1
            elif e in hashmap2:
                hashmap2[e]+=1   
        return hashmap1==hashmap2                 
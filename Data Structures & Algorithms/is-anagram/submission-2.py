class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1={}
        hashmap2={}
        for i1,e1 in enumerate(s):
            if e1 not in hashmap1:
                hashmap1[e1]=1
            elif e1 in hashmap1:
                hashmap1[e1]+=1

        for i2,e2 in enumerate(t):
            if e2 not in hashmap2:
                hashmap2[e2]=1
            elif e2 in hashmap2:
                hashmap2[e2]+=1            

        return hashmap1==hashmap2        
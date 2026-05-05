class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        subset=[]
        def dfs(open,close):
            if close>open:
                return
            if close==n and open==n:
                result="".join(subset.copy())
                res.append(result)
                return
            if open<n:
                subset.append("(")
                dfs(open+1,close)
                subset.pop()
            if close<open:
                subset.append(")")
                dfs(open,close+1)  
                subset.pop()  
        dfs(open=0,close=0)
        return res        



           
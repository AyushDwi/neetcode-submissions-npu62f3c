
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            res=[]

            q=collections.deque()
            q.append(root)

            while q:
                 qLen=len(q)
                 level=[]
                 for i in range(qLen):
                        node=q.popleft()
                        if node:
                           level.append(node.val)
                           q.append(node.left)
                           q.append(node.right)
                 if level:

                     res.append(level)        
            return res
                                                                                                                                                                                                   

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        bfs_ans=self.levelOrder(root)
        for i in bfs_ans:
                res.append(i[-1])
        return res

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.cusum=0
        self.l=[]
        self.ans=[]
        def dfs(node):
            if node==None:
                return 
            self.cusum+=node.val
            self.l.append(node.val)    
            if node.left==None and node.right==None:
                if self.cusum==targetSum:
                    self.ans.append(self.l[:])    
            
            dfs(node.left)
            dfs(node.right)
            self.cusum-=node.val
            self.l.pop()
        dfs(root)
        return self.ans
        
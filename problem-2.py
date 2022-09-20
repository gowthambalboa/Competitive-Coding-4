#tc: O(n)
#sc: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # base
        if root is None: return True
        
        #logic
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        if(abs(leftHeight-rightHeight) > 1): return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
            
        
    def getHeight(self,root):
        # base
        if root is None: 
            return 0
        # logic
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
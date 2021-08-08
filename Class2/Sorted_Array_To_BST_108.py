class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        if len(nums) == 0:
            return
        return self.createTree(nums, 0, len(nums)-1)

    def createTree(self, nums, start, end):
        if start > end:
            return
        mid = int(start + (end - start)/2)
        node = TreeNode(nums[mid])
        node.left = self.createTree(nums, start, mid-1)
        node.right = self.createTree(nums, mid+1, end)
        return node

if __name__ == '__main__':
    s1 = Solution()
    node = s1.sortedArrayToBST([1,2,3,4,5,6,7])
    print(node.val)
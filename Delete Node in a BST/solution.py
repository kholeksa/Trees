class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == key:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            if root.left and root.right:
                root.val = self.minimal(root.right)
                root.right = self.deleteNode(root.right, root.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root

    def minimal(self, node):
        while node.left:
            node = node.left
        return node.val

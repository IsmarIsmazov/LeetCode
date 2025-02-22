class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: Optional[TreeNode]
        """
        stack = []
        i = 0

        while i < len(traversal):
            depth = 0
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1

            value = 0
            while i < len(traversal) and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1

            # Create a new node
            node = TreeNode(value)

            while len(stack) > depth:
                stack.pop()

            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            stack.append(node)

        return stack[0]

        # return self.recover_tree(traversal)

    # def recover_tree(self, traversal):
    #     if not traversal:
    #         return None

    #     idx = traversal.find('-')
    #     if idx == -1:
    #         return TreeNode(int(traversal))

    #     root = TreeNode(int(traversal[:idx]))

    #     left_subtree_start = idx
    #     while left_subtree_start < len(traversal) and traversal[left_subtree_start] == '-':
    #         left_subtree_start += 1

    #     right_subtree_start = left_subtree_start
    #     depth = 0
    #     while right_subtree_start < len(traversal):
    #         if traversal[right_subtree_start] == '-':
    #             depth += 1
    #         else:
    #             if depth > 1:
    #                 break
    #             depth = 0
    #         right_subtree_start += 1

    #     root.left = self.recover_tree(traversal[left_subtree_start:right_subtree_start])
    #     root.right = self.recover_tree(traversal[right_subtree_start:])

    #     return root


# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def recoverFromPreorder(self, traversal):
#         """
#         :type traversal: str
#         :rtype: Optional[TreeNode]
#         """
    #     return self.recover_tree(traversal)

    # def recover_tree(self, traversal):
    #     if not traversal:
    #         return None
    #     root = TreeNode(int(traversal[:traversal.find('-')]))
    #     root.left = self.recover_tree(traversal[traversal.find('-') + 1:])
    #     root.right = self.recover_tree(traversal[traversal.find('-') + 1:])
    #     return root
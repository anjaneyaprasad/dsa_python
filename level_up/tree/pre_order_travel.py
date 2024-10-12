def preorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    res = []

    def helper(node, result):
        if node is None:
            return result

        res.append(node.value)
        helper(node.left, result)
        helper(node.right, result)
        return result

    return helper(root, res)

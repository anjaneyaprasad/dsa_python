from level_up.tree.insert_bst import insert_bst, insert_bst1


def postorder_traversal(root):
    temp = root
    visited = set()
    while temp and temp not in visited:
        if temp.left and temp.left not in visited:
            temp = temp.left
        elif temp.right and temp.right not in visited:
            temp = temp.right
        else:
            print(temp.value, end=" ")
            visited.add(temp)
            temp = root


def post_order_traversal(root):
    stack = [root]
    res = []

    while stack:
        node = stack[-1]
        if not node.left and not node.right:
            res.append(stack.pop().value)  # pop only when node has no children.
        else:
            if node.right:
                stack.append(node.right)
                node.right = None  # add the child to stack and set that relationship to None
            if node.left:
                stack.append(node.left)
                node.left = None

    return res


def main():
    root = insert_bst()
    result = post_order_traversal(root)
    print(result)

    root = insert_bst()  # otherwise below traversal gives last element only.
    postorder_traversal(root)
    print()

    root1 = insert_bst1()
    print(post_order_traversal(root1))


if __name__ == '__main__':
    main()

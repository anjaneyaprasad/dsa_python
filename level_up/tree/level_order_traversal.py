from level_up.tree.insert_bst import insert_bst, insert_bst1


def level_order_traversal(root):
    result = []
    q = []
    if root is None:
        return result
    q.append(root)
    while q:
        level_size = len(q)
        temp = []
        while level_size > 0:
            node = q.pop(0)
            temp.append(node.value)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            level_size -= 1
        result.append(temp)
    return result


def main():
    root = insert_bst()
    result = level_order_traversal(root)
    print(result)

    root1 = insert_bst1()
    result = level_order_traversal(root1)
    print(result)


if __name__ == '__main__':
    main()

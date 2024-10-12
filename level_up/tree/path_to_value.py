from level_up.tree.insert_bt import insert_bt


def path_to_value(root, value):
    result = []

    def helper(node, slate, node_value):
        slate.append(node.value)

        if node_value == node.value:
            print('found')
            result.extend(slate[:])

        if node.left and not node.right:
            print('left')
            helper(node.left, slate, node_value)
            slate.pop()
        elif node.right and not node.left:
            print('right')
            helper(node.right, slate, node_value)
            slate.pop()
        elif node.left and node.right:
            print('non-leaf')
            helper(node.left, slate, node_value)
            slate.pop()
            helper(node.right, slate, node_value)
            slate.pop()

    if root is None:
        return result
    helper(root, [], value)
    return result


def main():
    root = insert_bt()
    print(path_to_value(root, 2))


if __name__ == '__main__':
    main()

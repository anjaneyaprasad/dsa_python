def delete(root, value):
    if root is None:
        return None

    # case 1: leaf node
    curr = root
    prev = None

    while curr != None:
        if value == curr.value:
            print("match found: " + str(curr.value))
            break

        if value < curr.value:
            prev = curr
            curr = curr.left
            print("curr value left: " + str(curr.value))
        else:
            prev = curr
            curr = curr.right
            print("curr value right: " + str(curr.value))

    if curr is None:
        return root

    if curr.left is None and curr.right is None:
        print("Has no childs")
        if prev == None:
            return None

        if curr is prev.left:
            prev.left = None
            print("Deleted...!")
        else:
            prev.right = None
            print("Deleted...!")

    # case 2: node has one child
    child = None

    if curr.left is None and curr.right is not None:
        print("Has only right child")
        child = curr.right
    elif curr.left is not None and curr.right is None:
        print("Has only right child")
        child = curr.left

    if child is not None:
        if prev is None:
            root = child
            return

    if curr is prev.left:
        prev.left = child
        print("Deleted...!")
    else:
        prev.right = child
        print("Deleted...!")

    return root

    # case 3: node has two children
    if curr.left is not None and curr.right is not None:
        print("Has both childs..!")
        prev = curr
        succ = curr.right
        while succ.left is not None:
            prev = succ
            succ = succ.left

        curr.key = succ.key

        if succ is prev.left:
            prev.left = succ.right
        else:
            prev.right = succ.right

        return root



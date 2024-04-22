def tree_by_levels(node):
    if node is None:
        return []
    
    result = []
    queue = [node]

    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result
    

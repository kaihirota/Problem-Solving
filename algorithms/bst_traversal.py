def inOrderTraverse(tree, array):
    def DFS(tree):
		if tree:
			DFS(tree.left)
			array.append(tree.value)
			DFS(tree.right)

	DFS(tree)
    return array

def inOrderTraverse(tree, array):
	current = tree
    done = 0
	stack = []

    while True:
		if current is not None:
			stack.append(current)
			current = current.left
        elif(stack):
			current = stack.pop()
            array.append(current.value)
            current = current.right
        else:
			break

	return array

def preOrderTraverse(tree, array):
    def DFS(tree):
		if tree:
			array.append(tree.value)
			DFS(tree.left)
			DFS(tree.right)

	DFS(tree)
    return array


def postOrderTraverse(tree, array):
    def DFS(tree):
		if tree:
			DFS(tree.left)
			DFS(tree.right)
			array.append(tree.value)

	DFS(tree)
    return array

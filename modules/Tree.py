class Tree:
    def __init__(self, value, left=None, right=None, data=None):
        self.value = value
        self.data = data
        self.left = left
        self.right = right

    def __str__(self) -> str:
        def pprint(node, prefix="", is_left=True):
            result = prefix + ("└── " if is_left else "┌── ") + str(node.value) + "\n"
            if node.right:
                result += pprint(node.right, prefix + ("    " if is_left else "│   "), False)
            if node.left:
                result += pprint(node.left, prefix + ("    " if is_left else "│   "), True)
            return result

        return pprint(self).rstrip()
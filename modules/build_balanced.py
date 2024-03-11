from modules.Tree import Tree


def build_balanced(nodes):
  if not nodes:
    return False
  middle = len(nodes) // 2
  left = nodes[: middle]
  right = nodes[middle + 1:]
  balanced = Tree(nodes[middle], build_balanced(left), build_balanced(right))
  return balanced
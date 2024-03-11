import copy
from modules.Tree import Tree


def find_node(tree: Tree, value: int):
  node: Tree = copy.copy(tree)
  while node:
    if node.value == value:
        return node
    if value < node.value:
        node = node.left
    else:
        node = node.right
  return "NOT FOUND"
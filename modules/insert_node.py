def insert_node(tree, new_node):
  node = tree
  while node:
    last_node = node
    if new_node.value > last_node.value:
      node = node.right
    else:
      node = node.left

  if new_node.value > last_node.value:
    last_node.right = new_node
  else:
    last_node.left = new_node
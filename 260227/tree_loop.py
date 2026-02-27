def preorder(nodes, idx, result):
  if idx >= len(nodes):
    return result
  
  result.append(nodes[idx])
  preorder(nodes, idx * 2 + 1, result)
  preorder(nodes, idx * 2 + 2, result)
  
  return result

def inorder(nodes, idx, result):
  if idx >= len(nodes):
    return result
  
  inorder(nodes, idx * 2 + 1, result)
  result.append(nodes[idx])
  inorder(nodes, idx * 2 + 2, result)

  return result

def postorder(nodes, idx, result):
  if idx >= len(nodes):
    return result
  
  postorder(nodes, idx * 2 + 1, result)
  postorder(nodes, idx * 2 + 2, result)
  result.append(nodes[idx])
  return result

print(preorder([1,2,3,4,5,6,7], 0, []))
print(inorder([1,2,3,4,5,6,7], 0, []))
print(postorder([1,2,3,4,5,6,7], 0, []))
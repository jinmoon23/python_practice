class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def insert(root, val):
  if root is None:
    return Node(val)
  if val < root.val:
    root.left = insert(root.left, val)
  elif val > root.val:
    root.right = insert(root.right, val)
  
  return root
  
def search(root, val):
  if root is None: return False
  if val == root.val: return True

  if val < root.val:
    return search(root.left, val)
  return search(root.right, val)


def solution(lst, search_lst):
  root = None
  for val in lst:
    root = insert(root, val)

  return [search(root, val) for val in search_lst]

print(solution([5,3,8,4,2,1,7,10], [1,2,5,6]))
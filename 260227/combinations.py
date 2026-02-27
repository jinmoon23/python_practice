def combinations(arr, r):
  result = []
  picked = []

  def backtrack(start):
    if (len(picked) == r): 
      result.append(picked[:])
      return
    
    for i in range(start, len(arr)):
      picked.append(arr[i])
      backtrack(i + 1)
      picked.pop()
  
  backtrack(0)
  return result

print(combinations(["a", "b", "c", "d", "e"], 2))
def is_group_complete(m,i,j):
  if i > len(m) - 2:
    return False

  if j > len(m[0]) - 2:
    return False

  return True

def occupied(m, i, j):
  if m[i][j] is None:
    return 0
  
  return 1

def is_single_group(m,i,j):
  result = 0

  result += occupied(m, i, j)
  result += occupied(m, i+1, j)
  result += occupied(m, i, j+1)
  result += occupied(m, i+1, j+1)

  return result == 1
  

def rotate_group(m,i,j):

  origin_value = m[i][j]
  
  m[i][j] = m[i+1][j]
  m[i+1][j] = m[i+1][j+1]
  m[i+1][j+1] = m[i][j+1]
  m[i][j+1] = origin_value

def iteration(n,m):
  offset = n % 2

  for row in range(len(m)):
    if row % 2 != offset:
        continue
    
    for col in range(len(m[0])):
      if not is_group_complete(m, row, col):
        continue

      if not is_single_group(m, row, col):
        continue
  
      if col % 2 != offset:
        continue
      
      rotate_group(m, row, col)


  

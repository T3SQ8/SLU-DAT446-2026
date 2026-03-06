def is_group_complete(m,i,j):
  if i > len(m) - 2:
    return False

  if i > len(m[0]) - 2:
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


# Ifall du vill se lösningen på denna rekommenderas GitLab:n med tentafrågor eller komma på onsdagspasset
def iteration(n,m):
  pass

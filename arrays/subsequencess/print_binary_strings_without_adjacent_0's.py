def sequence(index, current):
  if index>=n:
    r.append("".join(current))
    return 
  current.append("1")
  sequence(index+1, current)
  current.pop()
  if index==0 or current[-1] =="1":
    current.append("0")
    sequence(index+1, current)
    current.pop()

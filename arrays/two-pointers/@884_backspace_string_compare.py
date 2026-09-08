def back(s, t):
  def build(string):
    s =[]
    for i in string:
      if i!= '#':
        s.append(i)
      elif s:
        s.pop()
    return s
  return build(s) == build(t)

# TC = O(M+N)
# SC = O(M+N)
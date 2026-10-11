def generate(n):
  r=[]
  def parenthesis(open_count, close_count, sub):
    if len(sub) == 2*n:
      r.append("".join(sub))
      return 
    if open_count<n:
      sub.append("(")
      parenthesis(open_count+1, close_count, sub)
      sub.pop()
    if close_count<open_count:
      sub.append(")")
      parenthesis(open_count, close_count+1, sub)
      sub.pop()
  parenthesis(0, 0, [])
  return r
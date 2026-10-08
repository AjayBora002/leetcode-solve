# no 111, 110, 011
def sequence(index, current):
  if index>=n:
    r.append("".join(current))
    return
  current.append("0")
  sequence(index+1, current)
  current.pop()
  if index ==0 or current[-1] == "0":
    current.append("1")
    sequence(index+1, current)
    current.pop()

n=3
r=[]
sequence(0, [])
print(r)


def lengy(stri):
  i = len(stri)-1
  while i>=0 and stri[i] == " ":
    i-=1
  length = 0
  while i>=0 and stri[i] != " ":
    length+=1
    i-=1
  return length









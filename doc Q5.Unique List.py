def unique_list(l):
  b= []
  for a in l:
      if a not in b:
        b.append(a)
  return b
print(unique_list([1,2,3,3,3,3,4,5])) 

def match_words(words):
  i=0
  for word in words:
    if len(word)>1 and word[0]==word[-1]:
      i+= 1
  return i
print(match_words(['abc', 'xyz', 'aba', '1221',]))





a=["abc","abcda","1201","abta"]
i=0
c=0
for word in a:
  if len(word)>1 and word[0]==word[-1]:
    c=c+1
  i+=1
print(c)

















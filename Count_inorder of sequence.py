s = "AppViewXXaaA"
#print(len(re.findall("a", s)))
#print(s.count('b'))

l = len(s)
for i in range(l):
  c,f_s = 0,s[0]
  for j in range(len(s)):
    if f_s == s[j]:
      c += 1
      if j == len(s)-1 or s[j] != s[j+1]:
        break
  print(f_s+str(c),end="")
  s = s[j+1:]
  if s == "":
    break
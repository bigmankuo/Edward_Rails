s1=input()
sums=0
for i in range(len(s1)):
  sums += ord(s1[i])
  print("ASCII code for '{}' is {}" .format(s1[i], ord(s1[i])))
print(sums)
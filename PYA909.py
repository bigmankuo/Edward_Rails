s1 = list()
for i in range(5):
	s1 += [input()]


with open("data.dat", "w", encoding="utf-8") as fn:
    for i in range(len(s1)):
        fn.write(str(s1[i])+"\n")
            
with open("data.dat", "r", encoding="utf-8") as fn:
  s2 = fn.read()
s2 = s2.replace("\n","\n\n")
print('The content of "data.dat":')
print(s2)
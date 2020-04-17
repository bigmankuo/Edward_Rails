s1 = list()
for i in range(5):
	s1 += [input()]


with open("data.dat", "w") as fn:
    for i in range(len(s1)):
        if i < len(s1)-1:
            fn.write(str(s1[i])+"\n\n")
        else:
            fn.write(str(s1[i]))
            
with open("data.dat", "r") as fn:
  s2 = fn.read()

print('The content of "data.dat":')
print(s2)
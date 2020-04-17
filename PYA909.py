s1 = list()
for i in range(5):
	s1 += [input()]

with open("data.dat", "w") as fn:
    for item in s1:
        fn.write(str(item)+"\n")

with open("data.dat", "r") as fn:
  s2 = fn.read()

print(s2)
s1 = dict()
s2= list()
for i in range(10):
    s2.append(int(input()))
    s1[s2[-1]]= 0

for i in range(len(s2)):
    s1[s2[i]] += 1

s3= list(s1.keys())
s4= list(s1.values())

print(s3[s4.index(max(s4))])
print(max(s4))
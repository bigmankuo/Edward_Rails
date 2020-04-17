fn = input()
f1 = open(r"C:\Python\test\read2.txt",encoding="utf-8")
#f1 = open(fn,encoding="utf-8")
cj = int(input())
datas = f1.read()
datas = datas.replace("\n"," ")
w1 = datas.split(" ")
c1 = [0] * len(w1)

for i in range(len(w1)):
    c1[w1.index(w1[i])] += 1

wsmeetcj = sorted([w1[i] for i in range(len(c1)) if c1[i]==cj])
#wsmeetcj = list()
#for i in range(len(c1)):
#    if c1[i]==cj:
#        wsmeetcj.append(w1[i])

#wsmeetcj = sorted(wsmeetcj)
for i in range(len(wsmeetcj)):
    print(wsmeetcj[i])



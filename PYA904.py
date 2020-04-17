f1 = open(r"C:\Python\test\read1.txt")
datas = f1.read()
t0 = list()
t0 = datas.split("\n")
h1 = list()
w1 = list()
for i in range(len(t0)):
    t0[i] = t0[i].split(" ")
for i in range(len(t0)):
    for j in range(len(t0[i])):
        if t0[i][j].isdigit() == True:
            t0[i][j] = eval(t0[i][j])
            if j == 1:
                h1.append(t0[i][j])
            elif j == 2:
                w1.append(t0[i][j])
print(datas.replace("\n","\n\n"))
print("Average height: {:.2f}" .format(sum(h1)/len(h1)))
print("Average weight: {:.2f}" .format(sum(w1)/len(w1)))
print("The tallest is {} with {:.2f}cm".format(t0[h1.index(max(h1))][0],max(h1)))
print("The heaviest is {} with {:.2f}kg" .format(t0[w1.index(max(w1))][0],max(w1)))
f1.close()


f1 = open(r"C:\Python\test\read.txt")
datas = f1.read()
ld = list(eval(datas.replace(" ",",")))
print(ld,"\n",sum(ld))
f1.close()

f1 = open("read.txt")
print(sum(list(eval(f1.read().replace(" ",",")))))
f1.close()
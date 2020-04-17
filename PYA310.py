n=int(input())
a=0
for i in range(n-1):
    a += 1/((i+1)**0.5+(i+2)**0.5)

print("{:.4f}" .format(a))

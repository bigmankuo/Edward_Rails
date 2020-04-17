a=int(input())
b=float(input())
m=int(input())

print("Month 	  Amount")
p = a
for i in range(m):
    p += p*b/1200 
    print("{:^5d}    {:8.2f}" .format(i+1, p))

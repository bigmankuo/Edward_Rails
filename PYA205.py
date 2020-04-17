a=int(input())
b=float(input())
m=int(input())

print("Month 	  Amount")
for i in range(m):
    print("{:^5d} \t{:8.2f}" .format(i+1, a*(1+b*(i+1)/12)))

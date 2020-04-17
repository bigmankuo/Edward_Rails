v1 = 0
v2 = 0
vz = 0
for i in range(5):
    a = eval(input())
    if a == 1: 
        v1+=1
    elif a == 2: 
        v2+=1
    else: 
        vz += 1
    print("Total votes of No.1: Nami =  {}" .format(v1))
    print("Total votes of No.2: Chopper =  {}" .format(v2))
    print("Total null votes =  {}" .format(vz))
if v1 > v2:
    winner = "No.1: Nami"
elif v1 < v2:
    winner = "No.2: Chopper"
else:
    winner = "No one"
print("=> {} won the election." .format(winner))

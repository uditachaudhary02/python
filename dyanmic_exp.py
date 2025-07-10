total=0
exp=[]
num=int(input("enter exps"))
for i in range(num):
    exp.append(float(input("exp")))

total=sum(exp)
print("spent",total)
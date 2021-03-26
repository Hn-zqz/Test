import random
data=""
count=0
max=int(input("?"))
while count<max:
	da=random.randint(0,9)
	data=data+str(da)
	count+=1
print(len(data),data)
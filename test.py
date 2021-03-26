import random
data=""
count=0
max=5
while count<max:
	da=random.randint(0,9)
	data=data+str(da)
	count+=1
print(len(data),data)

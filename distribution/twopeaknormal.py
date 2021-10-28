value_list=[];
ini_pool1=[]
for i in range(100000):
	x=np.random.normal(loc=Normal_loc1, scale=Normal_scale1);
	while (x < 0 or x > 1):
		x=np.random.normal(loc=Normal_loc1, scale=Normal_scale1);
	ini_pool1.append(x)
ini_pool2=[]
for i in range(100000):
	x=np.random.normal(loc=Normal_loc2, scale=Normal_scale2);
	while (x < 0 or x > 1):
		x=np.random.normal(loc=Normal_loc2, scale=Normal_scale2);
	ini_pool2.append(x)

for i in range(Distribution_number):
	temp1=np.array([ini_pool1[np.random.randint(len(ini_pool1)-1)] for j in range(Agent_number_n)]);
	temp2=np.array([ini_pool2[np.random.randint(len(ini_pool2)-1)] for j in range(Agent_number_n)]);
	temp=[]
	for j in range(len(temp1)):
		if(random.randint(0, 1)):
			temp.append(temp1[j])
		else:
			temp.append(temp2[j])
	value_list.append(temp);

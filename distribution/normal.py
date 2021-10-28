


value_list=[];
ini_pool=[]
for i in range(100000):
	x=np.random.normal(loc=Normal_loc, scale=Normal_scale);
	while (x < 0 or x > 1):
		x=np.random.normal(loc=Normal_loc, scale=Normal_scale);
	ini_pool.append(x)
	
value_list=[];

for i in range(Distribution_number):
	temp=np.array([ini_pool[np.random.randint(len(ini_pool)-1)] for j in range(Agent_number_n)]);
	value_list.append(temp);



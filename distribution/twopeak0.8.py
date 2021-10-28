

def two_peak_normal_distribution(ii):
		
	return random.randint(0, 1)*0.8;
	
	
def value_two_peak_normal_distribution():
	list_temp=[np.random.rand(Agent_number_n) for i in range(Agent_number_n)];
	for ii in range(len(list_temp)):
		list_temp[ii]=two_peak_normal_distribution(ii)
		
	list_temp=np.array(list_temp)
	return list_temp;
print(value_two_peak_normal_distribution())



value_list=[];
for i in range(Distribution_number):
	temp=value_two_peak_normal_distribution()
	value_list.append(temp);




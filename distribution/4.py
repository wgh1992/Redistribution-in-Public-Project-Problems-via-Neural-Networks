value_list=[];
for i in range(Distribution_number):
	temp1=np.random.normal(loc=0.2, scale=0.05,size=Agent_number_n);
	temp2=np.random.normal(loc=0.4, scale=0.05,size=Agent_number_n);
	temp3=np.random.normal(loc=0.6, scale=0.05,size=Agent_number_n);
	temp4=np.random.normal(loc=0.8, scale=0.05,size=Agent_number_n);
	temp=[]
	for j in range(len(temp1)):
		x=random.randint(0, 3)
		if(x==0):
			temp.append(temp1[j])
		elif(x==1):
			temp.append(temp2[j])
		elif(x==2):
			temp.append(temp3[j])
		elif(x==3):
			temp.append(temp4[j])
	value_list.append(temp);

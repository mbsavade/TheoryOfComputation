#Number of a's is divisible by 2
print("Number of a's is divisible by 2\n\n")
while 1:
	ip=input("ENTER THE STRINGS OF a's AND b's :\nOR\nENTER q TO EXIT\n")#input option
	if ip=='q': #EXIT CONDITION
		break
	
	split_a=[] #STORE NO. OF a's
	split_b=[] #STORE NO. OF b's

	for i in ip:
		if i=='a':
			split_a.append(i) #ADD a's
		elif i=='b':
			split_b.append(i) #ADD b's

	
	if len(split_a)%2==0: #CONDITON TO SATISFY
                
		print ("\nACCEPTED\n") #IF CONDITION SATISFIED

	else:
		print ("\nREJECTED\n") #IF CONDITION NOT SATISFIED
		


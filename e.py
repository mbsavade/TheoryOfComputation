# No of a's are divisible by 4 and b's are not divisible by 3
print ("No of a's are divisible by 4 and b's are not divisible by 3\n")#HEADING
while 1:
	ip=input("\nENTER THE STRINGS OF a's AND b's :\nOR\nENTER q TO EXIT\n")
	if ip=='q': #EXIT CONDITION
		break
	
	split_a=[] #STORE NO. OF a's
	split_b=[] #STORE NO. OF b's

	for i in ip:
		if i=='a':
			split_a.append(i) #ADD a's
		elif i=='b':
			split_b.append(i) #ADD b's

	print ("a's: ",len(split_a),"b's: ",len(split_b)) #PRINT NUMBER OF a's AND b's
	
	if len(split_a)%4==0 and len(split_b)%3!=0: #CONDITON TO SATISFY
                
		print ("\nACCEPTED") #IF CONDITION SATISFIED

	else:
		print ("\nREJECTED") #IF CONDITION NOT SATISFIED
		

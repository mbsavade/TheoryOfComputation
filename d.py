# Binary number are divisible by 5
print ("Binary numbers Divisible by 5\n") #HEADING
while 1:
	ip=input("\nENTER THE BINARY NUMBER:\nOR\nEnter q for exit\n") #INPUT BINARY NUMBER
	if ip=='q': #EXIT CONDITION
		break
	
	digit=0 #STORE DECIMAL OF BINARY NUMBER
	count=len(ip)-1

	for i in ip:
		if i=='1':
			digit+=(2**count) #BINARY TO DECIMAL CONVERSION
		count -=1
	print (digit)
	if digit%5==0:
		print ('\nBINARY NUMBER is ',ip,' = ',digit,'IS DIVISIBLE BY 5\n\nACCEPTED') #IF CONDITION IS SATISFIED
	else:
		print ('\nBINARY NUMBER is ',ip,' = ',digit,'IS NOT DIVISIBLE BY 5\n\nREJECTED') #IF CONDITION NOT SATISFIED			

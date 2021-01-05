rupee=0
while 1:
	ip= input('\n\nSelect the Soda you want to drink\n\n!!YOU SHOULD CHOOSE THE SODA WORTH MORE THAN Rs.125!!\n\n1.Mountain Dew = Rs.25\n\n2.Red Bull = Rs.100 \n\nEnter your choice:\n')
	
	if ip=='1':
		rupee+=25

	elif ip=='2':
		rupee+=100
	
	
	if rupee!=125:
		print ('\n\nRs.',rupee)
		
	if rupee>=125:
		print ('\nRs.',rupee,'\nYOU HAVE SUCCESSFULLY ORDERED THE SODAS\nVISIT AGAIN')
		break

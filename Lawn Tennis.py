
print("\n\n\n                                                                  !!!!WELCOME TO THE LAWN TENNIS TOURNAMENT!!!!\n\n\n                                                     ")
s=0 #server initialized
o=0 #opponent initialized
while(s<=40 and o<=40): #conditions checked
	if(s==40 and o==40):
		break
	point=input("ENTER WHO SCORED\n\n1.SERVER\n2.OPPONENT\n") #MENU
	print("\n")
	if(point =='1'): #if server is selected
		if(s==40):
			break
		elif(s==30):
			s=s+10
			print("Scorecard\nServer = ",s," : Opponent",o)
		else:
			s=s+15
			print("Scorecard\nServer = ",s," : Opponent",o)     
	if(point=='2'):
		if(o==40):
			break
		elif(o==30):
			o=o+10
			print("Scorecard\nServer = ",s," : Opponent",o)
		else:
			o=o+15
			print("Scorecard\nServer = ",s," : Opponent",o)
if(s==40 and o<40):
	print("\n!!!!CONGRATULATIONS SERVER WON THE MATCH!!!!\n") #WINNING MESSAGE for Server
elif(o==40 and s<40):
	print("\n!!!!CONGRATULATIONS OPPONENT WON THE MATCH!!!!\n") #WINNING MESSAGE for Server
else:
	stie=0 
	otie=0
	print ("\n\n       OHHH!!!!  THE MATCH IS TIED  !!!!\n\n")
	print("                                                                    !!!TIE-BREAKER ROUND!!!                                                                                                ")
	while(stie<=2 and otie<=2): #TIE CONDITIONS
		if(stie==2):
			print("\n!!!!CONGRATULATIONS SERVER WON THE MATCH!!!!\n")
			break
		elif(otie==2):
			print("\n!!!!CONGRATULATIONS OPPONENT WON THE MATCH!!!!\n")
			break
		else:
			tie=input("ENTER WHO SCORED\n\n1.SERVER\n2.OPPONENT\n\n")
			if(tie=="1"):
				stie=stie+1
				otie=-1
				print("Scorecard\nServer = ",stie )
			if(tie=="2"):
				otie=otie+1
				stie=-1
				print("Scorecard\nOpponent",otie)

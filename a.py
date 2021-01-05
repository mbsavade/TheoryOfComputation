#Equal number of a's followed by equal number of b's
print ("Equal number of a's followed by equal number of b's\n\n")
while 1:
        ip = input("ENTER STRINGS OF a's AND b's\nOR\nEnter q to exit\n") #INPUT
        if ip == 'q':
                break
        split = [] #For storing array
        split_a=[] #For a 
        split_b=[] #For b

        for i in ip:
                if i=='a':
                        split.append(i)
                        split_a.append(i) #adding a to array
                elif i=='b':
                        split.append(i)
                        split_b.append(i) #adding b to array
        
        if len(split_a) != len(split_b): #Condition to be checked
                print("REJECTED\n\n")  #If condition is True
                
        elif split.index('a')> split.index('b'): #If b comes before a
                print("REJECTED\n\n")
                
        else:
                print("ACCEPTED\n\n")  #If condition is False

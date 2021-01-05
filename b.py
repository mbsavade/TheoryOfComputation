#First and last letter are same
print ("First and last letter are same\n")
while 1:
    ip = input('\nENTER THE STRINGS OF a & b:\nENTER q FOR EXIT:\n')
    if ip == 'q':
        break
    split = [] #Declaring array
    split_a = [] #declaring array for a
    split_b = [] #declaring array for b

    for i in ip:
        if i == 'a':
            split.append(i)
            split_a.append(i)
        elif i == 'b':
            split.append(i)
            split_b.append(i)

    if split[0] == split[-1]: #condition to be satisfied
        print('\nACCEPTED') #if condition is true
    else:
        print('\nREJECTED') #ifcondition is false

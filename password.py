def verify(a):
    flag1=0
    flag2=0
    flag3=0
    flag4=0
    for i in a:
        if(i>="A" and i<="Z"):
            flag1=1
        elif(i>="a" and i<="z"):
            flag2=1
        elif(i=="@" or i=="#" or i=="$" or i=="%" or i=="&" or i=="_"):
            flag3=1
        elif(i>="0" and i<="9"):
            flag4=1
    if(flag1==1 and flag2==1 and flag3==1 and flag4==1):
        print("valid password")
    else:
        print("not valid password")

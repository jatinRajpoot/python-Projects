import NumberSys as num
Num=num.Decimal()
print(''' 
                                         Welcome To the Calculator Made by Jatin
    ''')
while(True):
    print(""" 
                                    1. Press 1 To Convert Decimal to Hexadecimal                
                                    2. Press 2 To Convert Decimal to Octal                                            
                                    3. Press 3 To Convert Decimal to Binary                                         
                                    4. Press 4 To Convert Octal  to Decimal                                
                                    5. Press 5 To Convert Binary  to Decimal                    
                                    6. press ANY other key To Exit                                 
                                                    
    """)
    choose=int(input("Enter your choice\n"))
    if choose==1:
        print(" Enter the NO. Convert Decimal to Hexadecimal ")
        inp=int(input(" Enter Here .."))
        print(f" Your input is {inp} and ans is {Num.Decimaltohex(inp)} ")
    elif choose==2:
        print(" Enter the NO. Convert Decimal to Octal ")
        inp=int(input(" Enter Here .."))
        print(f" Your input is {inp} and ans is {Num.DectoOct(inp)} ")
    elif choose==3:
        print(" Enter the NO. Convert Decimal to Binary ")
        inp=int(input(" Enter Here .."))
        print(f" Your input is {inp} and ans is {Num.DectoBin(inp)} ")
    elif choose==4:
        print(" Enter the NO. Convert octal to Decimal ")
        inp=int(input(" Enter Here .."))
        print(f" Your input is {inp} and ans is {Num.OcttoDec(inp)} ")
    elif choose==5:
        print(" Enter the NO. Convert binary to Decimal ")
        inp=int(input(" Enter Here .."))
        print(f" Your input is {inp} and ans is {Num.BintoDec(inp)} ")  
    else:
        break
        
    

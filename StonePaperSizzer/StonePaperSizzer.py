import random as rn
import datetime as dt
todaydt=dt.date.today()
Player=0
computer=0
playername=input("Please Enter your name :-\n")
def game(comp,player): #Declare the Game result in use this in last
    win=0
    if(comp==player):
        print("Tie")
        win=2
    elif(comp=="s" and player=="z"):
        win=1
    elif(comp=="p" and player=="s"):
        win=1
    elif(comp=="z" and player=="p"):
        win=1
    else:
        pass
    return win
def ChangeNo(n): # it will change any no into a charter to comprare it later on 
    a=""
    if n==1:
        a="s"
    elif n==2:
        a="p"
    else:
        a="z"
    return a
def changeintofullname(a): # it will change the charter into its full name 
    temp=""
    if a=="s":
        temp="Stone"
    elif a=="z":
        temp="sizzer"
    else:
        temp="Paper"
    return temp
while(True): # infinite Loop 
    randno=rn.randint(1,3)
    print('''
    Press (s)Stone (p)Paper (z)Sizzer
    ''')
    a=input("")
    Comp=ChangeNo(randno)
    Result=game(Comp,a)
    print(f"You choose {changeintofullname(a)} and computer choose {changeintofullname(Comp)}")
    if Result==1:
        print("comp wins")
        computer+=1
    elif Result==2:
        print("Tie")
    else:
        print("You wins")
        Player+=1
    print(f"{playername} Score is {Player} and computer score is {computer}")
    if Player==10:
        break
    elif computer==10:
        break
Resultofthegame=""
if Player==10:
    Resultofthegame=f" ====>  {playername} Won the Game by {Player-computer}\n "
    print(Resultofthegame)
elif computer==10:
    Resultofthegame=f" ====>  Computer Won the Game by {computer-Player}\n "
    print(Resultofthegame)
with open("Score.txt","a") as file:
    Text=(f" ---------  This Game is played By {playername} On {todaydt} -------------\n \n ====>  The score of {playername} is {Player} And Score of Computer is {computer}\n \n")
    file.write(Text)
    file.write(Resultofthegame)



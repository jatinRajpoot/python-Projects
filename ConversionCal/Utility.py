'''
        The Utility Programme Provide the Necessary programs to the calculator 
        Every umportant program is listed below
'''
from numpy import multiply


def Reverse(string):  # Reverse function it willl help me Reverse the result made by the Lcm
        string=str(string)
        count=0
        F_RESULT=""
        for i in string: #Reversing the from down to up 
            count+=1
        for i in range(1,count+1):
            sign=-1
            i=i*sign
            F_RESULT+=string[i]
        return F_RESULT
def Final(number,number2):
    RESULT=LCM(number,number2)
    F_RESULT=Reverse(RESULT)
    return F_RESULT

def LCM(Divide,Divident): #  Give the Lcm of the of provide no.
        _TEMP_RESULT_=0
        RESULT=""
        while(Divide>0):
            _TEMP_RESULT_=Divide%Divident
            Divide=Divide//Divident
            if _TEMP_RESULT_==10:
                RESULT+="A"
            elif _TEMP_RESULT_==11:
                RESULT+="B"
            elif _TEMP_RESULT_==12:
                RESULT+="C"
            elif _TEMP_RESULT_==13:
                RESULT+="D"
            elif _TEMP_RESULT_==14:
                RESULT+="E"
            elif _TEMP_RESULT_==15:
                RESULT+="F"
            else:
                RESULT+=str(_TEMP_RESULT_)
        return RESULT

def Multiply(Multiply,Multiplied):
    Clone_Multiply=str(Multiply)
    sum1=0
    count=0
    _Temp_=0
    for i in Clone_Multiply:
        count+=1
    for i in range(0,count+1):
        _Temp_=Multiply%10
        sum1+=_Temp_*(Multiplied**i)
        Multiply=Multiply//10
    return sum1

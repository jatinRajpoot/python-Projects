from Utility import Final , Multiply
""" 
        Here i will write the class needed as i can call them multiple time again and again
        when ever i need these 

"""
class Decimal:
    @staticmethod
    def Decimaltohex(number):
        F_RESULT=Final(number,16)
        return F_RESULT
    @staticmethod
    def DectoOct(number):
        F_RESULT=Final(number,8)
        return F_RESULT
    @staticmethod
    def DectoBin(number):
        F_RESULT=Final(number,2)
        return F_RESULT
    @staticmethod
    def OcttoDec(number):
        r=Multiply(number,8)
        return r
    @staticmethod
    def BintoDec(number):
        r=Multiply(number,2)
        return r

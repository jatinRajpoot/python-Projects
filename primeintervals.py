_start=int(input("Enter Starting interval"))
_End=int(input("Enter Ending interval"))
def prime(n):
    Result="prime"
    nm=int(n/2+1)
    for i in range(2,nm):
        if n%i==0:
            Result="not prime"
            break
        else:
            Result="prime"
    if Result=="prime":
        return True
    else:
        return False
for i in range(_start,_End+1):
    if prime(i):
        print(i)
    else:
        pass


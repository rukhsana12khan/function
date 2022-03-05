def xyz(s,n):
    if n==0:
        print(s[o])
    else:
        print(s[n],end="")
        xyz(s,n-1)
s=input("enter")   
xyz(s,len(s-1))         
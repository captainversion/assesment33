def string(s):
    a={"uppercase":0, "lowercase":0}
    for b in s:
        if b.isupper():
           a["uppercase"]+=1
        elif b.islower():
           a["lowercase"]+=1
        else:
           pass
    print ("No. of Upper case characters : ", a["uppercase"])
    print ("No. of Lower case Characters : ", a["lowercase"])
string(input("enter the string:"))

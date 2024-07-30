import re
li=[]

email=input("Email: ")
li.append(email)

psw=input("Password: ")
li.append(psw)

item=li


print("login:")
for i in item:
    login=input(" ")
    if login==i:
        pass
    else:
        print("Invalid")


pattern=re.compile("[@.]")
regex=pattern.search(email)
if regex==pattern.search(email)==None:
    print("Does not look like Email")
else:
    pass




pattern=re.compile("com")
regex=pattern.search(email)
if regex==pattern.search(email)==None:
    print("invalid mail")
else:
    pass





pattern=re.compile("gmail")
regex=pattern.search(email)
if regex==pattern.search(email)==None:
    print("Does not look like Email")
else:
    pass


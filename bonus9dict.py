# we can also make the password checker using the python dictionaries
password= input("enter your password")

mydict={}  # this is to store the result of all constraints

# to check the length of password is greater than 8
if (len(password) >= 8) == True:
    mydict["length"]=True
else:
    mydict["length"]=False  # if not greater than return false

# to check if it contains digit or not we will iterate over the password string
# because isdigit method will not work on the string data type
d = False
for x in password:

    if x.isdigit():#==True:
        d=True

mydict["digits"] = d  # i write it outside of the for loop because it was executing again and again

# now to check if it contains at least capital letter or not
# we will use isupper method

c=False
for x in password:
    if x.isupper():#==True:
        c=True
mydict["capital"]=c

print(mydict)

if  all(mydict.values())== True:
    print("Strong Password")
else:
    print("weak Password")


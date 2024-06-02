password = input("enter your password")
result=[]# i will store all the constraints in a list

# to check the length of password is greater than 8
if (len(password) >= 8) == True:
    result.append(True)
else:
    result.append(False)  # if not greater than return false

# to check if it contains digit or not we will iterate over the password string
# because isdigit method will not work on the string data type
d = False
for x in password:

    if x.isdigit()==True:
        d=True

result.append(d)  # i write it outside of the for loop because it was executing again and again

# now to check if it contains at least capital letter or not
# we will use isupper method

c=False
for x in password:
    if x.isupper()==True:
        c=True
result.append(c)

if (all(result)) == True:
    print("Strong Password")
else:
    print("weak Password")





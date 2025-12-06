#takimg input from user and printing in formated string
boy_name=input("Enter boy name: ")
boy_age=int(input("enter boy age: "))
girl_name=input("Enter girl name: ")
girl_age=int(input("enter girl age: "))
age_difference=abs(boy_age-girl_age)
print(f"{boy_name} loves {girl_name} with age difference {age_difference} years")
#concatination
first_name="shreyas"
last_name="HS"
full_name=first_name+" "+last_name
print(full_name)
#repetation
a="Warning!! \n"*3
print(a)
#converting to upper case
b=" Shreyas HS "
print(b.upper())
print(b.lower())
print(b.strip())
print(b.replace("Shreyas","salaga"))
#using "" in the variables
c='''shreyas said "hi"
 salaga said "hi"'''
print(c)
#counting string length
print(len(b))

text="shreyas HS"
print(text[0])
print(text[-1])
print(text[0:7])
print(text[::2])

#escaping sequency
d="my name is shreyas\nshreyas is a good boy"
e="shreyas is a\tgood boy"
f="here we can print backslash \\"
print(d)
print(e)
print(f)


lgh=input("Enter your string :")
lkg=lgh.replace(" ","")
print(f"Number of character (excluding spaces):{len(lkg)}")






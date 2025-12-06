name="shreyas"
integer=12
float_value=52.676
boolian_type=True


#multiple variable assinment
g,f,h=12,23,43

#printing data type and the data
print(name)
print(type(name))

print(integer)
print(type(integer))

print(float_value)
print(type(float_value))

print(boolian_type)
print(type(boolian_type))

#adding the tho variables
print(integer+float_value)

#converting one data type to another data type
x=10
y=float(x)
print(type(y))

#airthmetic operator
a=10
b=12
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a**2)
print(a%b)
#boadmass rule 
print(a+b-a**a/b*a%b)
#swaping two variables by using third variable
k=123
l=324
print(f" before Swaping {k} and {l}")
temp=k
k=l
l=temp
print(f"after Swaping {k} and {l}")
#swaping two variables without using third variable
x=100
y=99
print(f"Value of x and y before swaping {x} and {y}")
x=x+y
y=x-y
x=x-y
print(f"Value of x and y after swaping {x} and {y}")

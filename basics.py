#07/12/2025
#assigning values to a variable 
a=10
b="Shreyas"
c=10.5
print(a)
print(b)
print(c)
#string literals 
name1="shreyas"
name2='shreyas'
name3='''Shreyas is 
a good boy'''
print(f" Name 1 = {name1} \n Name2={name2}\n Name3={name3}")
#int float bool literals  
num1=10
num2=10.25
num3=454154.5849846851651321658
num4=True
print(num1)
print(num2)
print(num3)
print(type(num4))

#special literals 
num5=None
print(type(num5))

#string concanitation 
stri="shreyas abc hs abcd"
print(stri[0:7])
print(stri.find("abcd"))
stri=stri.replace("abc hs abcd","hs")
print(stri)
stri2="word1,word2,word3"
print(stri2)
stri2=stri2.split(",")
print(stri2)

stri3="shreyas hs"
stri3=stri3.count("s")
print(stri3)


#tuple concanitation 
mytuple=(1,2,3,4,5,6)
mytuple1=(7,8)
mytuple+=mytuple1
print(mytuple)

#indexing on tuple
print(mytuple[2])

#slicing of tuple
print(mytuple[0:3])


#list
mylist=[1,2,3,4,5,6,7]
mylist1=(8,9)
mylist+=mylist1
mylist.extend([10,20,30])
print(mylist)
mylist.insert(3,255)
print(mylist)

#dictonary
dic={'name':'shreyas','age':19,'collage':'Reva university'}
print(dic)
print(dic.values())
print(dic.keys())
print(len(dic))

#sets
myset={1,2,3,45}
print(myset)
#union of two sets 
myset2={1,2,74,75}
print(myset | myset2)
#intersection  of two sets 
print(myset & myset2)
#diffrence of two sets 
print(myset - myset2)

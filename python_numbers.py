#there are 3 numeric type in python int, float, complex. (complex numbers are the numbers with "j" as the imaginary part)
x=19
y=57.4
z=7j
print("Int:",x)
print("Float:",y)
print("Complex:",z)

#you can convert these numbers from one type to other using int(), float() and complex() methods.
a=7
b=6.4
c=9j

print("Before converting:")
print(a)
print(b)
print(c)

#converting
p=float(a)
q=int(b)
r=complex(a)

print("After converting:")
print(p)
print(q)
print(r)

print(type(p))
print(type(q))
print(type(r)) 

#Python has a built-in module called random that can be used to make random numbers
import random
print(random.randrange(1,50)) # type: ignore

#----Exercise----
#1.You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python 
# and print it.
l=92
w=48.8
a=l*w
print("Area of football field:",a,"meters")

#2.You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 
# 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
packets=9
per_pack_cost=1.49
given=20
amount_spend=packets*per_pack_cost
return_amount=given-amount_spend
print("Shopkeeper will return",return_amount,"dollar")

#3.You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles 
# cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
s=5.5
area=s**2
rs=500
cost=area*rs
cost1=int(cost)
print("Total cost:",cost1,"rs")

#4.Print binary representation of number 17
num=17
binary=bin(num)
print("Binary representation of 17 is:",binary)
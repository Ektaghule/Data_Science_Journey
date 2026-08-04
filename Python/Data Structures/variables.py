#creating variables
e= 1200
f="ekta"
print(e)
print(f)

# variable can change type after they have been declared.
a=100
a="Hey"
print(a)

#you can declare variable by specifying the datatype, using casting.
x= int(5500)
y= str("This is my first python program")
print(x)
print(y)

#you can identify the variables datatype using the type() function
u= 700
d="Learning python"
print(type(u))
print(type(d))

#in python you can declare a string variable using single quotes or double quotes also.
s='Single quote string variable'
s1="Double quote string variable"
print(s)
print(s1)

#here variable names are case sensitive (q and Q are two different variables).
q=99
Q='Lemon'
print(q)
print(Q)

#----Exercise----
#1.Create two variables. One to store your birth year and another one to store current year. Now calculate 
# your age using these two variables.
birth_year=2004
current_year=2024
age=current_year-birth_year
print("My age is",age)

#2.Store your first, middle and last name in three different variables and then print your full name using 
# these variables.
fname="Ekta"
mname="Sham"
lname="Ghule"
name=fname+" "+mname+" "+lname
print(name)
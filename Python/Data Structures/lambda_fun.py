#lambda is a anonymous function which can take any number of arguments, but  can only  have a single expression
#syntax: lambda args: express
l1=lambda : print("Learning Python")
l1()

#lambda Function with an Argument
name=lambda fname: print("My name is", fname)
name("Ekta")

#Eg
x=lambda a:a+20
print(x(10))

y=lambda b,c: b*c
print(y(2,3))
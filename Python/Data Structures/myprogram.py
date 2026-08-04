import modules 
modules.greet("World")

#while importing module you can change its name too
import modules as md
md.add(10,15)

#dir function used to list all the function names in a module
y=dir(modules)
print(y)
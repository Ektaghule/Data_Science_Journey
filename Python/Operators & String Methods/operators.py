x=2
y=10

print(x+y) #addition
print(x/y) #division
print(x-y) #substraction
print(x*y) #multiplication
print(x // y) #floor division
print(x ** y) #exponentiation
print(x % y) #modulus (remainder)


x=5
y=10

print( x>=y) #greater than equal
print(x<=y) #less than equal
print(x==y) #equal
print(x!=y) #not equal
print(x>y) #greater than
print(x<y) #less than


x=10
y=20
z=30

print(x<y and y<z)
print(x>y or z>y)
print(not (x<z))

#Bitwise operator
x=10
y=5

print(x<<1) #Left shift
print(y>>1) #Right shift
print(x^y) #XOR
print(x&y) #AND
print(x|y) #OR
print(~x) #NOT


#Assignment operator
x=10
y=5

x+=y  #x=x+y
print(x)

x-=y #x=x-y
print(x)

x%=y #x=x%y
print(x)

x/=y #x=x/y
print(x)

x*=y #x=x*y
print(x)


#Membership operator
print('E' in 'Ekta')
print('k' not in 'Ekta')


#Identity operator
x=5
y=5

print(x is y)
print(x is not y)
print(id(x)) #points the memory address of variable x
print(id(y)) #points the memory address of variable y
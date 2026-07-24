#you can assign multiline string to a variable, using three quotes (you cand also use three single quotes)
x="""Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code 
readability with the use of significant indentation."""
print(x)

#strings in Python are arrays of bytes (accessing random character of string is called string slicing)
a= "Ice cream"
print(a[5])

#you can use len() function to get the length of the string
print(len(a))

#you can concatenate two string
s1="Hello"
s2="World"
s3=s1+s2
print(s3)

#now if you want space in between you can add it like this....
s4=s1+" "+s2
print(s4)

#----Exercise----
#1.Create 3 variables to store street, city and country, now create address variable to store entire address. 
# Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the 
# address in such a way that the street, city and country prints in a separate line
street="Main Street"
city="Anytown"
country="US"
address=street+"\n"+city+"\n"+country
print("Using +:",address)
address1=f"{street}\n{city}\n{country}"
print("Using f-string:",address1)

#2.Create a variable to store the string "Earth revolves around the sun"
#i.Print "revolves" using slice operator
#ii.Print "sun" using negative index
str="Earth revolves around the sun"
s1=str[6:14]
print("Slicing:",s1)
print("Negative index:",str[-4:])

#3.Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies 
# and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string 
# for this.
x=5
y=3
print(f"I eat {x} veggies and {y} fruits daily")

#4.I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the 
# correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones 
# and print the new string. Also try to do this in one line.
s="maine 200 banana khaye"
x=s.replace("200","10").replace("banana","samosa")
print(x)
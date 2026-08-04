#Comparison of strings
string1 = "orange"
string2 = "kiwi"

print(string1 == string2) #Equal to
print(string1 <= string2) #Less than equal to
print(string1 >= string2) #Greater than equal to
print(string1 < string2) #Less than
print(string1 > string2) #Greater than
print(string1 != string2) #Not equal to

#ord function is used to get the ascii code of the characters
ord("e")


#replace function
og_string = "Hey Ekta!"
new_string = og_string.replace("Hey","Hello")
print(new_string)


#Split function
sentence = "It's good weather outside"
word = sentence.split(" ")
print(word)
sentence2 = "Nice to meet you!"
word2 = sentence2.split(".")
print(word2)

#Formatting
date = 13
s1 = f"Hi, today's date is {date}"
print(s1)


#Strip function -> removes the white spaces from the begining and the end
s2="     Good evening"
print(s2.strip())


#Index function -> returns the index number of the specified string
s3="Ola it's me!"
index=s3.index("it's")
print(index)
index2 =s3.index("Hey")
print(index2)

#find function -> finds the string and returns the index number of it (The difference b/w index and find function is index gives error when the substring is not in the string and find function return -1 when the substring is not in the string)
s3="Ola it's me!"
find=s3.find("it's")
print(find)
find2 =s3.find("Hey")
print(find2)

s1="Welcome"
s2="Welcome123"
print(s1.isalpha())
print(s2.isalpha())


#count() -> returns how many time a character is there in the provided main string
s1="This is a string"
count=s1.count("a")
print(count)
s2="Riya loves to travel"
count2=s2.count("t")
print(count2)

s1="HELLO"
print(s1.isupper())

s2="HEllo"
print(s2.islower())

s3="abc123"
print(s3.isdigit())


s1="hello WORLD!"
swapped_txt=s1.swapcase()
print(swapped_txt)

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
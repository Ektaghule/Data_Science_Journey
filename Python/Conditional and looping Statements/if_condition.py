#if condition is written by using "if" keyword
a=20
b=10
if a>b:
    print("a is grater than b")

#Elif contidion, this condition means if the previous conditions are not true, then try this one
x=15
y=15
if x>y:
    print("x is greater than y")
elif x==y:
    print("x and y are equal")

#else keyword is used if any of the given conditions are not true
p=12
q=100
if p>q :
    print("p is greater than q")
elif p==q:
    print("p and q are equal")
else :
    print("q is greater than p")

#if..else condition
e=87
s=91
if e>s:
    print("e is greater than s")
else :
    print("s is greater than e")

#----Exercise----
#1.Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
#i.Write a program that asks user to enter a city name and it should tell which country the city belongs to
#ii.Write a program that asks user to enter two cities and it tells you if they both are in same country or 
# not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter 
# mumbai and dhaka it should print "They don't belong to same country"
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

def find_country(city):
    if city in india:
        return "India"
    if city in pakistan:
        return "Pakistan"
    if city in bangladesh:
        return "Bangladesh"
    else:
        return "City not found"

city=input("Enter the city name: ")
country=find_country(city)
print(f"{city} is in {country}")

city1=input("Enter the first city: ")
city2=input("Enter the second city: ")

country1=find_country(city1)
country2=find_country(city2)

if country1 == country2:
    print(f"Both cities are in {country1}")
else:
    print("They don't belong to same country")

#2.Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 
# 80 to 100. 
# i. Ask user to enter his fasting sugar level
# ii. If it is below 80 to 100 range then print that sugar is low
# iii. If it is above 100 then print that it is high otherwise print that it is normal
sugar_level=int(input("Enter your sugar level: "))

if sugar_level < 80:
    print("Sugar is low")
elif sugar_level > 100:
    print("Sugar is high")
else:
    print("Sugar is normal")
#for loop is used for iterating over a sequence of a list, a tuple, a dictionary, a set, or a string.
fruit=["apple","orange","kiwi"]
for i in fruit:
    print(i)

#Loop Through a String
lang="Python"
for x in lang:
    print(x)

#for loop with range() unction
val=range(6)
for v in val:
    print(v)

#----Exercise----
#1.After flipping a coin 10 times you got this result,
#result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
#Using for loop figure out how many times you got heads
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
head_count=0
for flip in result:
    if flip == "heads":
        head_count += 1
print("Number of heads:",head_count)

#2.Print square of all numbers between 1 to 10 except even numbers
for num in range(1,11):
    if num % 2!=0:
        print("Square of numbers except even numbers:",num*num)

#3.Your monthly expense list (from Jan to May) looks like this,
#expense_list = [2340, 2500, 2100, 3100, 2980]
#Write a program that asks you to enter an expense amount and program should tell you in which month that 
# expense occurred. If expense is not found then it should print that as well.
expense_list = [2340, 2500, 2100, 3100, 2980]
months=["Jan","Feb","March","April","May"]
user_input=int(input("Enter an expense amount: "))
for i in range(len(expense_list)):
    if expense_list[i]== user_input:
        print("Expense occured in: ",months[i])
        break
else:
    print("Expense not found")

#4.Lets say you are running a 5 km race. Write a program that,
# i.Upon completing each 1 km asks you "are you tired?"
# ii.If you reply "yes" then it should break and print "you didn't finish the race"
# iii.If you reply "no" then it should continue and ask "are you tired" on every km
# iv.If you finish all 5 km then it should print congratulations message
for i in range(1,6):
    tired=input(f"You ran {i}km! Are you tired? (Y/N): ")
    if tired == "Y":
        print("You didn't finish the race...")
        break
else:
    print("Congratulations! You finished the race.")


#5.Write a program that prints following shape
# *
# **
# ***
# ****
# *****
for i in range(1,6):
    print("*"*i)
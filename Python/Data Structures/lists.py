 #there are 4 built-in data types in Python used to store collections of data, which are  List, Tuple, Sets, and Dictionary, all with different qualities and usage.
#lists are used to store multiple values in a single variable
items=["apple","orange","kiwi","mango"]
print(items)

#you can access the list items through index munbers
print(items[2])

#you can also access the range of items from the list 
print(items[0:3])
print(items[-1])

#you can append(add) new items in the list using append() method
items.append("pineapple")

#you can get the number of items in the lists using len() function
print(len(items))

#how to join two lists
list1=["red","green","yellow"]
list2=["mysql","c","c++","python"]
l3=list1+list2
print(l3)

#you can check if a perticular item is present in the list or not using 'in' operator
print("kiwi" in items)
print("watermelon" in items)

#----Exercise----
#1.Let us say your expense for every month are listed below,
#January - 2200
#February - 2350
#March - 2600
#April - 2130
#May - 2190
#Create a list to store these monthly expenses and using that find out,
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction 
# to your monthly expense list based on this
listex=[2200,2350,2600,2130,2190]
print("1. Extra dallars spent in feb",listex[1]-listex[0])
print("2. Total expense in first quarter:",listex[0]+listex[1]+listex[2])
print(2000 in listex)
listex.append(1980)
listex[3]=listex[3]-200
print("5. After refund:",listex[3])

#2.You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,
# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',so remove it from the list first and 
# then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
# So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available 
# in list)
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append("black panther")
print(heros)
heros.remove("black panther")
print(heros)
heros.insert(3,"black panther")
print(heros)
heros[1:3]=["doctor strange"]
print(heros)
heros.sort()
print(heros)
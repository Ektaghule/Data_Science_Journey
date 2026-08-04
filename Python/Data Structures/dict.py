#Dictionaries are used to store data values in key:value pairs.
d1={
    "name":"Ekta",
    "surname":"Ghule",
    "fav_color":"pink"
}
print(d1)

#values can be referred to by using the key name.
print(d1["fav_color"])

#you can determine the number of items in the dictionaries using len() function
print(len(d1))

#to change the values, you just need to refer it's key name
d1["fav_color"]="blue"
print(d1)

#you can simply add new items without any function or method
d2={
    "fav_animal":"dog",
    "fav_flower":"rose"
}
d2["fav_movie"]="jab we met"
print(d2)

#you can chnage the values using the update() method
d2.update({"fav_animal":"cat"})
print(d2)

#you cant remove the items using the pop() method
d2.pop("fav_movie")
print(d2)

#----Exercise----
#1.We have following information on countries and their population (population is in crores),
#Country	Population
# China	143
# India	136
# USA	32
# Pakistan	21
#i.Using above create a dictionary of countries and its population
#ii. Write a program that asks user for three type of inputs,
#a) print: if user enter print then it should print all countries with their population in this format,
#china==>143
# india==>136
# usa==>32
# pakistan==>21
#b)add: if user input add then it should further ask for a country name to add. If country already exist in 
# our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population 
# and add that new country/population in our dictionary and print it
#c)remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary 
# then remove it and print new dictionary using format shown above in (a). Else print that country doesn't 
# exist!
#d)query: on this again ask user for which country he or she wants to query. When user inputs that country 
# it will print population of that country.
countries={
    "China":143,
    "India":136,
    "USA":32,
    "Pakistan":21
}

while True:
    user_input=input("Enter any option print, add, remove, query or exit: ").lower()

    if user_input == "print":
        for country, population in countries.items():
            print(f"{country}==>{population}")

    elif user_input == "add":
        country_name=input("Enter country name:")
        if country_name in countries:
            print("This name already exists!")
        else:
            population=int(input(f"Enter {country_name} population:"))
            countries[country_name]=population
            print(f"{country_name} added with {population} population..")

    elif user_input == "remove":
        country_name =input("Enter the country to be removed:")
        if country_name in countries:
            del countries[country_name]
            print(f"{country_name} is removed")
            for country, population in countries.items():
                print(f"{country}==>{population}")
        else:
            print(f"{country_name} does not exists")

    elif user_input == "query":
        country_name=input("Enter the country name to query:")
        if country_name in countries:
            print(f"Population of {country_name} is {countries[country_name]}")
        else:
            print(f"{country_name} does not exists")

    elif user_input == "exit":
        break
    else:
        print("Invalid input")

#2.You are given following list of stocks and their prices in last 3 days,
#Stock	Prices
#info	[600,630,620]
#ril	[1430,1490,1567]
#mtl	[234,180,160]
#i.Write a program that asks user for operation. Value of operations could be
#a)print: When user enters print it should print following,
#info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33
#b)add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list 
# (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your 
# dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.
stock_prices={
    "info":[600,630,620],
    "ril":[1430,1490,1567],
    "mtl":[234,180,160]
}

while True:
    user_input1=input("Enter print, add or exit: ").lower()

    if user_input1 == "print":
        for stock, prices in stock_prices.items():
            avg=sum(prices)/len(prices)
            print(f"{stock}==>{prices}==>avg:{avg:.2f}")

    elif user_input1 == "add":
        stock_name=input("Enter stock ticker:").lower()
        prices=int(input(f"Enter the prices for {stock_name}:"))
        
        if stock_name in stock_prices:
            stock_prices[stock_name].append(prices)
            print(f"Price added for {stock_name}..")
        else:
            stock_prices[stock_name]=prices
            print(f"{stock_name} is added with {prices} prices")

    elif user_input1 == "exit":
        break
    else:
        print("Invalid input")
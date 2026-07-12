# 6.1 Dictionary
# Dictionary is a ORDERED ,changeable and no duplicates set.

# Declare a dictionary
used_cars_prices = {
    "Model 3": 150000,
    "Porsche 911": 850000,
    "Toyota Camry": 80000,
    "Honda Civic": 75000,
}
# 6.1.1 get change and judge elements
alpha = used_cars_prices.get("Toyota Camry")
breakpoint = used_cars_prices.get("Mercerdes-Benz C-class") #None
print(
    f"Camry's price is {alpha},911's price is {used_cars_prices['Porsche 911']}"
)
used_cars_prices["Model 3"] = 140000
print(f'{"Model 3" in used_cars_prices} \n{"Nissan Altima" in used_cars_prices}')


# 6.1.2 traverse(遍历)
for i in used_cars_prices:
    print(i)  # print all key names
    print(used_cars_prices[i])  # print all values

for x, y in used_cars_prices.items():
    print(x, y)  # all key-values

# 6.1.3 append elements
used_cars_prices["BMW 325i"] = 220000
print(used_cars_prices)

# 6.1.4 delete elements
used_cars_prices.pop("Honda Civic")
print(used_cars_prices)

# 6.1.5 copy
used_car_prices_NY = used_cars_prices.copy()
used_car_prices_WA = dict(used_cars_prices)

# 6.1.6 dict in dict
president01 = {"name": "Bill Clinton", "start_year": 1993, "end_year": 2001}
president02 = {"name": "George W. Bush", "start_year": 2001, "end_year": 2009}
president03 = {"name": "Barack Obama", "start_year": 2009, "end_year": 2017}
presidents04 = {"name": "Donald Trump", "start_year": 2017, "end_year": 2021}
presidents = {
    "Clinton": president01,
    "Bush Jr.": president02,
    "Obama": president03,
    "Trump": presidents04,
}
print(presidents)
print(presidents["Bush Jr."]["start_year"])
# traverse dict in dict
for president, info in presidents.items():
    print(f"{president} was in office from {info['start_year']} to {info['end_year']}")

# 6.2 set
# set is a unordered,UNCHANGEABLE and NO DUPLICATES collection.
# 6.2.1 declare a set, use {}
eu_countries = {"UK","Germany", "France", "Italy", "Spain"}
## 6.2.2 add elements
eu_countries.add("Netherlands")
eu_countries.add("Austria")
eu_countries.add("Ireland")
# 6.2.3 delete elements
eu_countries.remove("UK") 
eu_countries.discard("UK")
# 6.2.4. traverse
for country in eu_countries:
    print(country)
# 6.2.5 judge if an element is in the set
print(f"Is Germany in the EU? {'Germany' in eu_countries}\nIs UK in the EU? {'UK' in eu_countries}")

# advantage using
nato_countries = {"USA", "Canada" ,"UK", "Germany", "France", "Italy", "Spain", "Netherlands"}

west_countries = nato_countries | eu_countries
print(f"western countries such as {west_countries}")
nato_not_eu = nato_countries - eu_countries
print(f"nato countries that are not in the EU: {nato_not_eu}")
eu_not_nato = eu_countries - nato_countries
print(f"eu countries that are not in the NATO: {eu_not_nato}")

both = nato_countries & eu_countries
print(f"countries that are in both NATO and EU: {both}")

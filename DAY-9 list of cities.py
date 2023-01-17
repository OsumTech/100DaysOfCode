#add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above


#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
city_list = []
new_country = {
    "Country": "",
    "Visits": "",
    "Cities": city_list,
}

name = input("Please Enter The Name of Country You Visited: ")
times = input("Please Enter How Many Times Have you Visited It: ")

def add_new_country(name, times,city_list):
    new_country ["Country"] = name
    new_country ["Visits"] = times
    add_city = True
    city_list = []
    while add_city:
        city = input("Please Enter The Cities You Visited Visited: ")
        city_list.append(city)
        want_add = input("Do You Want To Add More Cities? Y or N: ")
        if want_add == "n":
            add_city = False

add_new_country(name,times,city_list)
new_country["Cities"] = city_list
travel_log.append(new_country)

print(travel_log)

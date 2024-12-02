country = input("Add a country name. ") # Add country name
visits = int(input("Number of visits.")) # Number of visits
list_of_cities = eval(input("Create a list from formatted string. ")) # create list from formatted string

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
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 

def add_new_country(name_of_country, number_of_visits, list_of_visited_cities):
    new_country = {}
    new_country["country"] = name_of_country
    new_country["visits"] = number_of_visits
    new_country["cities"] = list_of_visited_cities
    travel_log.append(new_country)


# Do not change the code below 👇
add_new_country(name_of_country=country, number_of_visits=visits, list_of_visited_cities=list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
from ast import While


united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

united_kingdom [1]["capital"] = 'Cardiff'

print(united_kingdom)

list1 =   {
    "name": "Northern Ireland",
    "population": 1811000,
    "capital": "Belfast"
  }

united_kingdom.append(list1)


print(united_kingdom)

for number in united_kingdom:
     print(f'{number["name"]}')
    

total = 0
for pop in united_kingdom:
    total += pop["population"]

print(total)


# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
# 3. Use a loop to print the names of all the countries in the UK.
# 4. Use a loop to find the total population of the UK.

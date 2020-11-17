states = {
    'Vermont': 'VT',
    'Maryland': 'MD',
    'Rhode Island': 'RI',
    'Massachusetts': 'MA',
    'Tennessee': 'TN'
}

cities = {
    'VT': 'Williston',
    'MD': 'Baltimore',
    'RI': 'Providence',
    'MA': 'Boston',
    'TN': 'Nashville'
}

cities['VT'] = 'Williston'
cities['MD'] = 'Baltimore'
cities['RI'] = 'Providence'
cities['MA'] = 'Boston'
cities['TN'] = 'Nashville'

print('-' * 20)
print("VT has: ", cities['VT'])
print("MD has: ", cities['MD'])
print("RI has: ", cities['RI'])
print("MA has: ", cities['MA'])
print("TN has: ", cities['TN'])

print('-' * 20)
print("Vermont's abbreviation is: ", states['Vermont'])
print("Maryland's abbreviation is: ", states['Maryland'])
print("Rhode Island's abbreviation is: ", states['Rhode Island'])
print("Massachusetts's abbreviation is: ", states['Massachusetts'])
print("Tennessee's abbreviation is: ", states['Tennessee'])

for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

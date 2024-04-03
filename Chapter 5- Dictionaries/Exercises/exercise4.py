rivers = {
    'Nile': 'Egypt',
    'Amazon': 'United states',
    'Yangtze': 'China'
}

print("Sentences about each river:")
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nNames of each river:")
for river in rivers:
    print(river)

print("\nNames of each country:")
for country in rivers.values():
    print(country)

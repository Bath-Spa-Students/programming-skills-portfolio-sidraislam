def describe_city(city, country='Iceland'):
    """Describe a city and its country."""
    print(f"{city.title()} is in {country}.")

describe_city('reykjavik')
describe_city('bejeing', 'China')
describe_city('lahore', 'Pakistan')

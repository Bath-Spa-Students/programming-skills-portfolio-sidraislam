pets = [
    {'animal': 'cat', 'name': 'Mimi', 'owner': 'Amber'},
    {'animal': 'rabbit', 'name': 'Daisy', 'owner': 'Samra'},
    {'animal': 'dog', 'name': 'Ruby', 'owner': 'Isra'}
]
for pet in pets:
    print(f"\nHere's what I know about the {pet['animal']}:")
    for key, value in pet.items():
        print(f"{key}:{value}")
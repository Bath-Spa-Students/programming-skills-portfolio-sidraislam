# start with a list of guests
guests = ['Amber','samra','Isra','Ayesha']

#print invitation for each guest
print(guests[0].title()+",please come to my dinner party!")
print(guests[1].title()+",please come to my dinner party!")
print(guests[2].title()+",please come to my dinner party!")
print(guests[3].title()+",please come to my dinner party!")

# Ayesha can't make it, replace her
print("\n"+guests[3].title()+"can;t come.")
guests.remove('Ayesha')
guests.insert(3, 'Aliya')


# print invitations again
print("\n"+ guests[0].title() +"can't come.")
print(guests[1].title()+", please come to my dinner party!")
print(guests[2].title()+",please come to my dinner party!")

#Find a bigger dinner table
print("\nGood news, found a bigger dinner table!")

# Add guests to the end
guests.insert(0,'Laiba')
guests.insert(2,'khadija')
guests.append('Amna')

# print new invites
for guest in guests:
    print(guests)


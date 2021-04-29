person={
'first_name':"Yvonne",
'last_name':"Katama",
'age':26,
'city':"Nairobi"}
print(person['first_name'])
print(person['last_name'])
print(person.get('age'))
print(person.get('city'))
print(all(person))


favourite_numbers={'Paul':234,
'sheila':345,
'wesley':567,
'washington':3567,
'mercy':256}

favourite_numbers['wesley'.title()]=467
print(favourite_numbers)
print(any(favourite_numbers))
print(len(favourite_numbers))
print(sorted(favourite_numbers))
print(all(favourite_numbers))


favourite_food={
    'Eunice':"Pilau",
    'Mary':"mokimo",
    'Michelle':"Fish",
    'Phil':"Pilau",}
food=favourite_food['Mary'].title()
print(favourite_food.pop('Phil'))
print(f"Mary's favourite food is {food}.")
print(favourite_food)

price={}.fromkeys(['Apple','Banana','Kiwi','Orange'],80)
print(price)

for item in price.items():
    print(item)

print(list(sorted(price.keys())))



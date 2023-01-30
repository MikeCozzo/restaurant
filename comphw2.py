#CS175L
#Michael Cozzolino
#restaurant
Vegetarian = False
Vegan = False
Gluten_free = False

resp1 = input('is anyone in your party a vegetarian?')
if resp1 == 'yes':
    Vegetarian = True
resp2 = input('is anyone in your party a vegan?')
if resp2 == 'yes':
    Vegan = True
resp3 = input ('is anyone in your party gluten free?')
if resp3 == 'yes':
    Gluten_free = True
print('Here are your restaurant choices:')
if (not Vegetarian) and (not Vegan) and (not Gluten_free):
    print('Joes gourmet burgers')
elif (not Vegan) and (not Gluten_free):
    print('Mamas fine italian')
else: (not Vegan)
print('main street pizza')
print('corner cafe')
print('chefs kitchen')

print "Welcome to Pypet!"

name ='Fluffy'
age = 5
weight = 9.5
hungry = False
sleep = False
photo= '(=^o.o^=)__'


print 'Hello' + name
print photo

cat = {
'name': 'Fluffy' ,
'hungry': True,
'sleep': False
'weight': 9.5
'age': 5,
'photo': '(=^o.o^=)__'
}

mouse= {
'name':'Mouse',
'age': '7',
'weight': 1.5,
'sleep': False
'hungry': False,
'photo':'<:3 )----',
}

pets = [cat,mouse]

print 'Hello' + cat['name']
print cat['photo']

print cat

def feed(pet):
    if  pet['hungry'] == True:
        pet ['hungry'] = True
        pet ['weight'] = pet['weight'] + 1
    else:
        print 'The Pypet is not hungry!'

for pet in pets:
    feed(pet)
    print pet


    print cat
    feed(cat)
    print cat

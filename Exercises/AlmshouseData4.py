from collections import Counter
#More Bellevue Almshouse Cultural Analytics Activities
#This features real data, from the Bellevue Almshouse (which housed poor and homeless Irish immigrants in New York) from 1847 to 1849.
names = ['Unity', 'Catherine', 'Thomas', 'William', 'Patrick', 'Mary Anne', 'Morris',
        'Michael', 'Ellen', 'James', 'Michael', 'Hannah', 'Alexander', 'Mary A', 'Serena?',
        'Margaret', 'Michael', 'Jane', 'Rosanna', 'James', 'Michael', 'John', 'John', 'Mary',
        'Bantel', 'Marcella', 'Arthur', 'Michael', 'Mary', 'Martin']
last_names = ['Harkin', 'Doyle', 'McDonald', 'Jordan', 'Rouse', 'Keene', 'Brown',
               'McLoughlin', 'Cassidy', 'Whittle', 'Coyle', 'Cullen', 'Cozens', 
               'Maly', 'McGuire', 'Laly', 'Bahan', 'Combs', 'McGovern', 'Gallagher', 
               'Crone', 'Brannon', 'McDonal', 'Atkins', 'Garragan', 'Wood', 'Kelly', 'Galeny', 'Welch', 'Kerly']
diseases = ['', 'recent emigrant', 'sickness', '', '', '', 'destitution', '', 'sickness', '',
            'sickness', 'recent emigrant', '', 'insane', 'recent emigrant', 'insane', '', '',
            'sickness', 'sickness', '', 'syphilis', 'sickness', '', 'recent emigrant', 'destitution',
            'sickness', 'recent emigrant', 'sickness', 'sickness']
ages =    ['22', '21', '23', '47', '45', '28', '23', '50', '26', '28', '30', '30', '65', '17', '35',
        '27', '32', '40', '22', '30', '27', '40', '41', '37', '16', '20', '30', '30', '35', '19']

for disease in diseases:
    print(disease)

#Enurmerating:
for number, disease in enumerate(diseases):
    print(number, disease)

#With more specific data descriptions:
for number, disease in enumerate(diseases):
    print(f"Person #{number}: {disease}")

collection = ['fish', 'potatoes', 'fish', 'fish', 'potatoes']

#Appending
potatoes = []
for item in collection:
    if item == 'potatoes':
        potatoes.append(item)
print(potatoes)

#Appending, but applied to sickness:
sicknesses = []
for disease in diseases:
    if disease == 'sickness':
        sicknesses.append(disease)

print(sicknesses)
print(len(sicknesses)) #Tells you how many items are in the list.

#New Version of the Disease List:
diseases_updated = []
for disease in diseases:
    if disease == '':
        new_disease = 'no disease recorded'
        diseases_updated.append(new_disease)
    else:
        diseases_updated.append(disease)

print(diseases_updated)

#List Comprehension:
recent_emigrants = [disease for disease in diseases if disease == 'recent emigrant']
print(recent_emigrants)
print(len(recent_emigrants))

#Zipping:
for first_name, disease in zip(names, diseases_updated):
    print(f"{first_name}: {disease}")

for first_name, last_name, age, disease in zip(names, last_names, ages, diseases_updated):
    print(f"{first_name} {last_name}, age {age}: had {disease}")

#Dictionaries: Including every item in the list and every time they appear in the list.
print(Counter(diseases_updated))
#Sorting the dictionary:
tally = Counter(diseases_updated)
print(tally.most_common())
print(tally.most_common()[-2:])

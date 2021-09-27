from collections import Counter
#More Bellevue Almshouse Cultural Analytics Activities
#This features real data, from the Bellevue Almshouse (which housed poor and homeless Irish immigrants in New York) from 1847 to 1849.
shuffled_professions = ['married', 'married', 'laborer', 'laborer', 'widow', 'married', 'spinster',
                     'laborer', 'spinster', 'laborer', 'spinster', 'spinster', 'married', 'laborer',
                     'laborer', 'spinster', 'laborer', 'laborer', 'laborer', 'laborer', 'laborer', 'spinster',
                     'laborer', 'spinster', 'widow', 'spinster', 'painter', 'laborer', 'weaver', 'laborer']

#Exercise 17: Make a new list that includes only the items in the list of professions that matches "spinster."
spinsters = []
for profession in shuffled_professions:
    if profession == 'spinster':
        spinsters.append(profession)
print(spinsters)

#Exercise 18: Print out each item in the list next to an index.
for number, profession in enumerate(shuffled_professions):
    print(f"Person #{number}: {profession}")

#Exercise 19: Find the most common profession in the list.
tally = Counter(shuffled_professions)
print(tally.most_common(1))

#Exercise 20: Now find the least common.
tally2 = Counter(shuffled_professions)
print(tally.most_common()[-1:])

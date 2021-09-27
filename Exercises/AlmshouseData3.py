#For Loops practice with Almshouse Data
names = ['Mary', 'John', 'Anthony', 'Margaret']

for x in names:
    print(f"Hi! My name is {x}.")

ages = [28, 19, 60, 30]
for y in ages:
    if y > 30:
        print("I'm young!")
    else:
        print("I'm old!")
for z in ages:
    print(z * 2)

#More Bellevue Almshouse Cultural Analytics Activities
#This features real data, from the Bellevue Almshouse (which housed poor and homeless Irish immigrants in New York) from 1847 to 1849.
professions = ['married', 'laborer', 'widow', 'laborer']
genders = ['female', 'male', 'male', 'female']
children = ['Alana', 'Catherine', 'Charles', 'Riley']
child_status = ['Child', 'Child', 'No child', 'Child']

#Exercise 10: Extract the second item in the list of professions.
print(professions[1])

#Exercise 11: Add the term "spinster" (unmarried woman) to the professions list, then print.
professions.append('spinster')
print(professions)

#Exercise 12: Make a for loop that considers each item in the professions list.
for profession in professions:
    if profession == 'married':
        print("This person is married.")
    elif profession == 'laborer':
        print("This person is a laborer.")
    elif profession == 'widow':
        print("This person is a widow.")
    elif profession == 'spinster':
        print("This person is a spinster.")
    else:
        print("This person had another job.")

#Exercise 13: Extract the list of children's names, and print the fourth item.
print(children)
print(children[3])

#Exercise 14: Make a for loop that prints each child status from the original four names.
for child in child_status:
    if child == 'Child':
        print("This person has a child.")
    else:
        print("This person does not have a child.")

#Exercise 15: Add two items to the gender list - "non-binary" and "unknown."
genders.append('non-binary')
genders.append('unknown')
print(genders)

#Exercise 16: Create a for loop that considers each item in the gender list and prints the correct gender.
genders.append('mayonnaise') #IS MAYONNAISE A GENDER?

for gender in genders:
    if gender == 'male':
        print("This person is a male.")
    if gender == 'female':
        print("This person is a female.")
    if gender == 'non-binary':
        print("This person's gender does not conform to male/female binaries.")
    else:
        print("This person's gender is not known.")

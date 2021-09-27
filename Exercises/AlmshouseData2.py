names = ['Mary Gallagher', 'John Sanin', 'Anthony Clark', 'Margaret Farrell']
ages = [28, 19, 60, 30]
#Just to make sure they register correctly.
print(type(names))
print(type(ages))
#Indexing the list values:
print(names[0])
print(ages[3])
print(names[-1]) #Attempt at reverse-indexing, as covered briefly by Walsh in the textbook.

#Indexing a larger list.
people = ['Anna', 'Ben', 'Charles', 'Diana', 'Erik', 'Fred', 'Gina', 'Henry', 'Ian', 'Jane']
print(people[:2])
print(people[2:])
print(people[::3])
#Reverse! Reverse!
print(people[-2:])

#List methods:
people.append('Kurt')
print(people)
ages.sort(reverse=False)
print(ages)
ages.sort()
print(ages)
ages.sort(reverse=True)
ages.sort()

more_people = ['Laura', 'Michael', 'Natalie', 'Olivia', 'Paul', 'Quincy', 'Richard', 'Sophia', 'Thomas', 'Ursula', 'Victor', 'William', 'Xavier', 'Yolanda', 'Zach']
people.extend(more_people)
print(people)


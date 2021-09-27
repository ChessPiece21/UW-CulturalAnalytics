#Bellevue Almshouse Cultural Analytics Activities
#This features real data, from the Bellevue Almshouse (which housed poor and homeless Irish immigrants in New York) from 1847 to 1849.

#Person 1 Information:
Person1_Name = 'Mary Gallagher'
Person1_Age = 28
Person1_Disease = 'recent immigrant'
Person1_Profession = 'married'
Person1_Gender = 'female'
Person1_Child = 'Alana, 10 days old'

#Exercise 1: Write an if statement that reports whether this person is younger than 30 years old.
if Person1_Age < 30:
    print('1. ' + Person1_Name + ' is less than 30 years old.')
elif Person1_Age > 30:
    print('1. ' + Person1_Name + ' is over 30 years old.')
else:
    print('1. ' + Person1_Name + ' is 30 years old.')

#Exercise 2: Write an if statement that reports whether this person is married.
if Person1_Profession == 'married':
    print('2. ' + Person1_Name + ' is married.')
elif Person1_Profession == 'widowed':
    print('2 .' + Person1_Name + ' is widowed.')
else:
    print('2. ' + Person1_Name + ' is unmarried.')

#Exercise 3: Write an if statement that reports whether they are married AND younger than 30 years old.
if Person1_Age < 30 and Person1_Profession == 'married':
    print('3. ' + Person1_Name + ' is less than 30 years old and also married.')
elif Person1_Age < 30 or Person1_Profession == 'married':
    print('3. ' + Person1_Name + ' is either less than 30 years old or married.')
else:
    print('3. ' + Person1_Name + ' is neither less than 30 years old nor married.')

#Person 2 Information:
Person2_Name = 'Anthony Clark'
Person2_Age = 60
Person2_Disease = 'recent immigrant'
Person2_Profession = 'laborer'
Person2_Gender = 'male'
Person2_Child = 'Charles Riley, died after 10 days, aged 18'

#Exercise 4: Write a conditional that will report whether this person is older or younger than 30.
if Person2_Age < 30:
    print('4. ' + Person2_Name + ' is less than 30 years old.')
elif Person2_Age > 30:
    print('4. ' + Person2_Name + ' is over 30 years old.')
else:
    print('4. ' + Person2_Name + ' is 30 years old.')

#Person 3 Information:
Person3_Name = 'Margaret Ferrell'
Person3_Age = 30
Person3_Disease = 'recent immigrant'
Person3_Profession = 'widowed'
Person3_Gender = 'female'
Person3_Child = '' #Original dataset says NaN or Null depending on which reader I open it with (Excel or Google Sheets).

#Exercise 5: Write a conditional that will report the person's gender.
if Person3_Gender == 'female':
    print('5. ' + Person3_Name + ' is female.')
else:
    print('5. ' + Person3_Name + ' is male.')

#Exercise 6: Write an if statement that will report whether Person 1 and Person 3 have children.
if Person1_Child == 'Alana, 10 days old':
    print('6. ' + Person1_Name + ' has children.')

if Person3_Child == '':
    print('6. ' + Person3_Name + ' has no children.')

#Exercise 7: Write a single if statement that will accurately report whether a person has children.
Child_Status = [Person1_Child, Person3_Child] #It's an array with two values.
if Child_Status[0] != '':
    print('7. Person has children.')
if Child_Status[1] == '':
    print('7. Person has no children.')

#Exercise 8: Write a conditional that will report whether this person is married, a laborer, a widow, or unemployed.
#Then, test your code by reassigning variables.

#Profession = 'married'
#Profession = 'laborer'
#Profession = 'widowed'
Profession = 'student'

if Profession == 'married':
    print('8. Person is married.')
elif Profession == 'laborer':
    print('8. Person is working as a laborer.')
elif Profession == 'widowed':
    print('8. Person is widowed.')
else:
    print('8. Person is of an unknown profession.')

#Exercise 9: Clean up the data behind at least one unclear name or profession of your choice. Make that person Person 4.
Person4_Name = 'John Sanin(?)'

if '(?)' in Person4_Name:
    #print(Person4_Name.split('(?)')) - DOES NOT WORK
    print('9. ' + Person4_Name.replace('(?)', ''))

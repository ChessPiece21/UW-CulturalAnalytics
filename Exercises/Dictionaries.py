#Python Dictionary Example:
person1 = {"name": "Joe Lollo",
           "age": 22,
           "profession": "Student"}
print(type(person1)) #To make sure it runs.

person2 = {"name": "Joe Biden",
           "age": 79,
           "profession": "46th President of the United States"}

print(person2.keys())
print(person2.values())

person3 = {"name": "Borat Sadgiyev",
           "age": 49,
           "profession": "Deliverer of Prodigious Bribe to American Regime for Make Benefit Once Glorious Nation of Kazakhstan",
           "birthplace": "Kazakhstan"}

#print(person3)
print(person3["name"])
print(person3["age"])
print(person3["profession"])
print(person3["birthplace"])

person3["age"] = 50 #How old he'll be in a few months anyway.
person3["profession"] = "Television Anchorman"
print(person3)

#Nested Dictionary Using Key & Peele College Football Players:
nested_people = {
    "person4":
    {"name": "Rerutweeds Myth",
     "position": "Quarterback",
     "school": "Washington"},
    "person5":
    {"name": "Hingle McCringleberry",
     "position": "Safety",
     "school": "Penn State"},
    "person6":
    {"name": "Ozamatazz Buckshank",
     "position": "Runningback",
     "school": "Stanford"},
    "person7": #Note: not used until the printing part.
    {"name": "Dan Smith",
     "position": "Kicker",
     "school": "Brigham Young"}
    }
print(nested_people["person5"])
print(nested_people["person4"]["school"])
print(nested_people["person6"]["position"])

for person in nested_people.values():
        name = person["name"]
        school = person["school"]
        position = person["position"]
        print(f'On the roster for the East/West Bowl this year is {name}, a {position} from {school}.')

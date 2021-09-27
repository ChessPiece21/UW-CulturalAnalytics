def sing():
    print("Mining away")
    print("But I don't know what to mine")
    print("I'll mine anyway")
    print("In this Minecraft day, so beautiful")
    print("I'm further down...")
    print("...what is that I found?")
    return
sing()

print("") #Newline to separate.

def sing_birthday_song(personalized_name):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print(f"Happy Birthday dear {personalized_name}!")
    print("Happy Birthday to you!")
    return
sing_birthday_song("Anna")

print("")

def sing_birthday_song_with_keywords(toname = "Joe", fromname = "Your friends :)"):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print(f"Happy Birthday dear {toname}!")
    print("Happy Birthday to you!")
    print(f"Sincerely, \n{fromname}")
    return
sing_birthday_song_with_keywords()
print("")
sing_birthday_song_with_keywords(toname = "Beyonce", fromname = "Jay-Z")

print("")

#Exercise on text effects through Python as well as more complicated calculations.
def make_text_shouty(text):
    shouty_text = text.upper()
    return shouty_text
print(make_text_shouty("I like tacos"))

def make_text_shoutier(text):
    shouty_text = text.upper()
    shoutier_text = shouty_text + "!!!"
    return shoutier_text
print(make_text_shoutier("I like tacos"))

def calculate_dog_years_age(age):
    dog_years_age = age * 7
    return dog_years_age
print(calculate_dog_years_age(21))

def make_text_whispery(text):
    whispery_text = text.lower()
    return whispery_text
print(make_text_whispery("I AM WHISPERING."))

sample_text = open("Metamorphosis.txt", encoding="utf-8").read()

#Indexing: Grabbing a specific substring by character number.
print (sample_text[0])
print (sample_text[1])
print (sample_text[2])

#Slicing: Changing a string upbetween or up to certain characters.
print (sample_text[0:121])
print (sample_text[122:250])

#Creating a variable for the first sentence, so that the output is equivalent to "The Metamorphosis"'s first sentence.
sentence1 = sample_text[0:121]

print (sentence1)

#More String Methods:
print (sentence1.lower()) #lowercase
print (sentence1.upper()) #UPPERCASE
print (sentence1.title()) #Titlecase
print (sentence1.strip())
print (sentence1.split('.'))
print (sentence1.startswith('O'))
print (sentence1.endswith('!'))

#Word Replacement Time:
#OLD CODE:
#print (sentence1.replace('morning', 'evening'))
#print (sentence1.replace('vermin', 'potato'))

#NEW CODE:
sentence2 = sentence1.replace('morning', 'evening')
sentence3 = sentence2.replace('bed', 'oven')
sentence4 = sentence3.replace('vermin', 'potato')
print (sentence4)

#Splitting:
print(sentence1.split())
print(sentence1.split('dreams')) #Splitting with a delimiter - in this case, the word "dreams."

#Joining with a Delimiter:
split_words = sentence1.split()
print(split_words)
print('_'.join(split_words))

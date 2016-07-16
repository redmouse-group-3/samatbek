word = "Hello! My name is Samatbek. What is yours?"

word = word.split(' ')
maxWord = 0

i = 0
while i < len(word):
    if int(len(word[maxWord])) < int(len(word[i])):
        maxWord = i
    i += 1
print "'%s' is the longest word" % word[maxWord]
word = "Hi!; How do you do?; I wanted to talk with you;"
sep = raw_input("Please, enter separator: ")

word = word.split(sep)
minWord = 0

i = 0
while i < len(word):
    if int(len(word[minWord])) > int(len(word[i])):
        minWord = i
    i += 1
print "'%s' is the longest word" % word[minWord]
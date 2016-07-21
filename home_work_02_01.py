text = "apple samsung xiaomi lg meizu"

word = text.split(' ')
maxWord = word[0]

for x in word:
    if len(maxWord) < len(x):
        maxWord = x

print "'%s' is the longest word" % maxWord

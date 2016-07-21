text = "Apple Samsung Xiaomi LG Meizu"

words = text.split(' ')
max_word = words[0]

for x in words:
    if len(max_word) < len(x):
        max_word = x

print "'%s' is the longest word" % max_word

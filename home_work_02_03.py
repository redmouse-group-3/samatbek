text = "Java; C; PHP; Python; HTML; CSS"
sep = raw_input("Please, enter separator: ")

words = text.split(sep)
min_word = words[0]

for x in words:
    if min_word > x:
        min_word = x

print "'%s' is the shortest word" % min_word

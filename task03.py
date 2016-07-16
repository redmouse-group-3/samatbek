def split(word):
    word = word.split(' ')
    for i in word:
        print('%s - %d' % (i, len(i)))

text = raw_input("Enter text: ")
split(text)


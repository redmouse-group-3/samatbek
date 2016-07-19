def split(text):
    word = text.split(' ')
    for i in word:
        print('%s - %d' % (i, len(i)))

text = raw_input("Enter text: ")


split(text)


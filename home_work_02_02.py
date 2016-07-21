text = "Java;C;PHP;Python;HTML;CSS"

words = text.split(';')
max_word = words[0]

for x in words:
    if max_word < x:
        max_word = x

print "'%s' is the longest word" % max_word

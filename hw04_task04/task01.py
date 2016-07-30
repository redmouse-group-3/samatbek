import random
import re
from sys import exit


def get_rand_words():
    words = (random.sample(['samsung', 'apple', 'motorolla', 'lenovo', 'lg', 'meizu', 'xiaomi', 'oneplus'], 8))
    return ' '.join(words)


def get_first_word(string):
    return str(re.findall(r'^\w+', string)[0])


def get_last_word(string):
    return str(re.findall(r'\w+$', string)[0])


def reverse_first(string, word):
    return re.sub(r'^\w+', word[::-1], string)


def reverse_last(string, word):
    return re.sub(r'\w+$', word[::-1], string)


text = get_rand_words()

print('text before: %s' % text)

user_word = raw_input("Enter word: ")

if user_word == get_first_word(text):
    text = reverse_first(text, user_word)
elif user_word == get_last_word(text):
    text = reverse_last(text, user_word)
else:
    print "Invalid input!"
    exit(0)

print('text after:  %s' % text)

import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Get input from the user
user_input = input("Enter a sentence for POS tagging: ")

# Tokenize the user input and perform POS tagging
words = word_tokenize(user_input)
pos_tags = pos_tag(words)

print(pos_tags)
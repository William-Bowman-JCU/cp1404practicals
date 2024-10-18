"""
Word Occurrences
Estimate: 20 minutes
Actual:   15 minutes
"""

text = input('Text: ')
words = sorted(text.split())
word_to_occurrences = {}
for word in words:
    if word in word_to_occurrences:
        word_to_occurrences[word] += 1
    else:
        word_to_occurrences[word] = 1

for word in word_to_occurrences:
    print(f'{word:10} : {word_to_occurrences[word]}')
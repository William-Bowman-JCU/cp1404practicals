"""
Word Occurrences
Estimate: 20 minutes
Actual:   15 minutes
"""

text = input('Text: ')
words = sorted(text.split())
words_dict = {}
for word in words:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

for word in words_dict:
    print(f'{word:10} : {words_dict[word]}')
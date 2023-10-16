import pandas
import re
import pyperclip
import json
words_list = pandas.read_csv('words.csv')

words = words_list["Word"].to_list()
# print(words)
wordRegex = re.compile(r'(\w+)')
words_with_translation = []
counter = 0
for word in words:
    wordReg = wordRegex.findall(word)
    words_with_translation.append(wordReg)

# print(words_with_translation)

translations = []

for word in words_with_translation:
    new_word = {
        "word": {"character": word[2], "translation": word[1], "romanized": word[3]}}
    translations.append(new_word)
strings = json.dumps(translations, ensure_ascii=False)
# pyperclip.copy(strings)

# print(translations)

import json
from collections import defaultdict
import os


def clear():
    os.system('cls')


user_path = 'C:/Users/Isabelle/AppData/Local/plover/plover/user.json'
main_path = 'C:/Users/Isabelle/AppData/Local/plover/plover/main.json'

user_dictionary_unmapped = json.load(open(user_path, encoding='utf-8'))
main_dictionary_unmapped = json.load(open(main_path, encoding='utf-8'))

user_dictionary = defaultdict(list)
main_dictionary = defaultdict(list)

for k, v in user_dictionary_unmapped.items():
    user_dictionary[v].append(k)
for k, v in main_dictionary_unmapped.items():
    main_dictionary[v].append(k)

clear()
while True:
    word_to_search = input("\n\nFind Word:").strip()

    clear()
    header = '+++  ' + word_to_search + '  +++'
    print(header)
    print('-' * len(header))
    if word_to_search in user_dictionary:
        for result in user_dictionary[word_to_search]:
            print(result)
    elif word_to_search in main_dictionary:
        for result in main_dictionary[word_to_search]:
            print(result)
    elif word_to_search == 'quit()':
        clear()
        break
    else:
        print('no results')
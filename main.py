import json
from difflib import get_close_matches


def load_dictionary():
    dictionary = json.load(open("Data/words.json"))
    return dictionary


def find_word(input_word):
    dictionary = load_dictionary()
    input_word = input_word.lower()
    if input_word in dictionary:
        print(f"{input_word.capitalize()}:")
        for definition in dictionary.get(input_word):
            print(definition)
    else:
        close_match = get_close_matches(input_word, dictionary.keys(), n=1)
        if close_match:
            confirmation = input(f"The word doesn't exist in the dictionary. Did you mean {close_match[0]}? Press Y or N.")
            if confirmation.lower() == "y":
                find_word(close_match[0])
        else:
            print("The word doesn't exist in the dictionary.")


if __name__ == '__main__':
    word = input("Enter a word: ")
    find_word(word)


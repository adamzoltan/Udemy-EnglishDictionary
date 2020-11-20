import json


def load_dictionary():
    dictionary = json.load(open("Data/words.json"))
    return dictionary


def find_word(input_word):
    dictionary = load_dictionary()
    print(f"{input_word.capitalize()}:")
    for definition in dictionary[input_word]:
        print(definition)


if __name__ == '__main__':
    word = input("Enter a word: ")
    find_word(word)


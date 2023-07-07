dictionary = {
    "apple": "A fruit that grows on trees and is typically red or green.",
    "banana": "A long curved fruit with a yellow skin.",
    "cat": "A small domesticated carnivorous mammal with soft fur.",
    "dog": "A domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, and a barking, howling, or whining voice.",
}

def search_word(word):
    if word in dictionary:
        return dictionary[word]
    else:
        return "The word '{}' does not exist in the dictionary.".format(word)

def run_dictionary_app():
    print("Welcome to the Python Dictionary App!")
    print("Enter a word to look up its definition.")
    print("To exit the app, enter 'exit'.")

    while True:
        user_input = input("Enter a word or 'exit' to exit the app: ")

        if user_input.lower() == "exit":
            print("Thank you for using the Python Dictionary App. Goodbye!")
            break

        definition = search_word(user_input)
        print(definition)

run_dictionary_app()

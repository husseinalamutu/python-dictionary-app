# Python Dictionary App

The Python Dictionary App is a simple command-line application that allows users to look up the definitions of words. Users can input a word, and the app will search its internal dictionary database to retrieve and display the corresponding definition(s). The app provides a user-friendly interface for easy interaction.

## Features

- Accepts user input: The app prompts the user to enter a word they want to look up in the dictionary.
- Displays definitions: Upon receiving user input, the app searches its internal dictionary database for the word's definition(s) and displays them in a well-formatted manner.
- Handles non-existent words: If the entered word does not exist in the dictionary database, the app provides a meaningful message to inform the user.
- Graceful exit: Users have the option to exit the app gracefully by entering a predefined command ("exit" or "quit") or by using a keyboard shortcut.

## Prerequisites 

`
Python 3.x
`

## Getting Started
Clone the repository:

_bash_

```
git clone https://github.com/your-username/python-dictionary-app.git
```

Navigate to the project directory:

_bash_

```
cd python-dictionary-app
```

Run the app:

_bash_

```
python dictionary_app.py
```

Usage

    When the app starts, you will see the following message:

    Welcome to the Python Dictionary App!
    Enter a word to look up its definition.
    To exit the app, enter 'exit'.

    Enter a word that you want to look up and press Enter.

    The app will display the definition(s) of the entered word, if available in its dictionary.

    If the entered word does not exist in the dictionary, the app will display a message indicating that the word is not found.

    To exit the app, enter "exit" or "quit".

## Customization 1

You can customize the app by modifying the dictionary variable in the dictionary_app.py file. Add or remove word-definition pairs to suit your needs. The dictionary follows a key-value structure, where the key is the word and the value is the corresponding definition.

Example:

python

```
dictionary = {
    "car": "A motor vehicle with four wheels, typically powered by an internal combustion engine.",
    "guitar": "A stringed musical instrument played with the fingers or a plectrum, typically having six strings.",
    "book": "A written or printed work consisting of pages glued or sewn together along one side and bound in covers.",
    "computer": "An electronic device that is capable of storing, processing, and retrieving data.",
}
```

Feel free to update the dictionary with your own word-definition pairs.

## Customization 2: Using a JSON File as the Database

You can also create a .json file to save your word-definition pairs. This file will serve as the database for your words. Here's how you can do it:

1. Create a new file in the same directory as dictionary_app.py and name it dictionary.json.

2. Open the dictionary.json file in a text editor and add your word-definition pairs in the following format:

```
{
    "word1": "definition1",
    "word2": "definition2",
    "word3": "definition3",
    ...
}
```

### Example:

```
{
    "apple": "A fruit that grows on trees and is typically red or green.",
    "banana": "A long curved fruit with a yellow skin.",
    "cat": "A small domesticated carnivorous mammal with soft fur.",
    "dog": "A domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, and a barking, howling, or whining voice."
    "chair": "A piece of furniture designed for sitting on, typically having a back and four legs.",
    "computer": "An electronic device that is capable of storing, processing, and retrieving data.",
    "pencil": "A narrow cylinder of wood or graphite used for writing or drawing.",
    "butterfly": "A flying insect with large, brightly colored wings.",
    "telephone": "A system for transmitting voices over a distance using wire or radio.",
    "planet": "A celestial body moving in an elliptical orbit around a star.",
    "music": "The art form of organized sound, often incorporating melody, rhythm, and harmony.",
    "cake": "A sweet baked dessert often decorated and enjoyed for celebrations.",
    "camera": "A device used for capturing and recording visual images.",
    "rainbow": "A meteorological phenomenon that creates a spectrum of colors in the sky after rain."
}
```
Add as many words and definitions as you like to the JSON file.

3. Save the dictionary.json file.

4. In the dictionary_app.py file, replace the dictionary variable with the following code:

```
import json

def load_dictionary():
    with open("dictionary.json") as file:
        return json.load(file)

dictionary = load_dictionary()
```

This code will load the word-definition pairs from the dictionary.json file into the dictionary variable.

You can now run the app, and it will use the word-definition pairs from the dictionary.json file as its database.

## License

This project is licensed under the MIT License.

## Acknowledgements

- This app was created as an assignment for learning purposes.
- The app is based on the assignment requirements and uses a simplified approach to demonstrate the functionality of a dictionary app.

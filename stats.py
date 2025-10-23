def get_num_words(text: str):
    return len(text.split())

def count_characters(text: str):
    characters = {}

    for character in text:
        if character.lower() not in characters:
            characters[character.lower()] = 1
        else:
            characters[character.lower()] += 1
    
    return characters

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

def parse_dictionary_to_list(dictionary: dict):
   list_of_characters = []

   for character in dictionary:
    if character.isalpha():
        list_of_characters.append({
            'char': character,
            'num': dictionary[character]
        })

   return list_of_characters

def create_alphanum_list(characters: dict):
    list_of_characters = parse_dictionary_to_list(characters)

    list_of_characters.sort(reverse=True, key=sort_on)

    return list_of_characters
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
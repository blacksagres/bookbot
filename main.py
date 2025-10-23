from stats import get_num_words, count_characters

FRANKENSTEIN_BOOK_PATH = './books/frankenstein.txt'

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()

def main():
    book_text = get_book_text(FRANKENSTEIN_BOOK_PATH)
    word_amount = get_num_words(book_text)

    print(f'Found {word_amount} total words')

    character_count = count_characters(book_text)

    print(character_count)


main()

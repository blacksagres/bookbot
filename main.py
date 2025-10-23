from stats import get_num_words, count_characters, create_alphanum_list

FRANKENSTEIN_BOOK_PATH = './books/frankenstein.txt'

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()

def main():
    book_text = get_book_text(FRANKENSTEIN_BOOK_PATH)
    word_amount = get_num_words(book_text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")

    print(f'Found {word_amount} total words')

    print("--------- Character Count -------")

    character_count = count_characters(book_text)
    for item in create_alphanum_list(character_count):
        print(f"{item['char']}: {item['num']}")


    print('============= END ===============')


main()

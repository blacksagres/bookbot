from stats import get_num_words, count_characters, create_alphanum_list
import sys


def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()

def main():

    if len(sys.argv) != 2:
        print('📜 Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    # finding args - main.py books/frankenstein.txt
    book_path = sys.argv[1]

    if book_path is None:
        print('❌ Book path not provided, exiting the bot.')
        sys.exit(1)


    book_text = get_book_text(book_path)
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

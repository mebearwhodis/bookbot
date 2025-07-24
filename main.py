import sys
from stats import (
    chars_dict_to_sorted_list, 
    get_characters_dict, 
    get_words_count
    )

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    text = get_book_text(book_path)
    words_count = get_words_count(text)
    characters_dict = get_characters_dict(text)
    sorted_characters_list = chars_dict_to_sorted_list(characters_dict)
    print_report(book_path, words_count, sorted_characters_list)


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(book_path, words_count, sorted_characters_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for item in sorted_characters_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()
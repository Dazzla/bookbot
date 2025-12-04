import sys
from stats import get_num_words, count_each_character, sort_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text():
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        return file.read()

def main():
    #print(get_book_text())
    num_of_words = get_num_words(get_book_text())
    #print(f"Found {num_of_words} total words.")
    #print(count_each_character(get_book_text()))
    print_sorted_list(sort_list(get_book_text()))

def print_sorted_list(sorted_list):
    num_of_words = get_num_words(get_book_text())
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_of_words} total words
--------- Character Count -------""")
    for item in sorted_list:
        if item['char'].isalpha():  # Print only alphabetic characters
            print(f"{item['char']}: {item['num']}")

main()
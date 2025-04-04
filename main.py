from stats import count_words, count_chars
import os, sys

def get_book_text (filepath: str) -> str:
    with open(filepath) as file:
        return file.read()

def main():
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        print("============ BOOKBOT ============")
        print("----------- Word Count ----------")
        total_words = count_words(get_book_text(book_path))
        print(f"Found {total_words} total words")
        print("--------- Character Count -------")    
        char_count_dict = count_chars(get_book_text(book_path))
        for key in char_count_dict.keys():
            print(f"{key}: {char_count_dict[key]}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()
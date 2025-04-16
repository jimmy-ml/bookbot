import sys
from stats import count_words, get_book_text, character_dict_sort

def main():
    if len(sys.argv) != 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    character_list = character_dict_sort(book_text)
    for character in character_list:
        if not character['character'].isalpha():
            continue
        print(f"{character['character']}: {character['count']}")
    print("============= END ===============")
main()
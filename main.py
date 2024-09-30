def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = "books/frankenstein.txt"
    print(read_book(book))

main()


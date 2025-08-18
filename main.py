from stats import get_characters, count_words

def get_book_file(path):
    with open(path, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def main():
    path = "books/frankenstein.txt"
    count_words(get_book_file(path))
    count_char = get_characters(path)
    print(count_char)

main()

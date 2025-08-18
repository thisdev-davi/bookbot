from stats import count_words

def get_book_file(path):
    with open(path, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def main():
    count_words(get_book_file("books/frankenstein.txt"))

main()

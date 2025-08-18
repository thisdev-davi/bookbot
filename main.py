def get_book_file(path):
    with open(path, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def count_words_file(file):
    num_words = len(file.split())
    print(f"{num_words} words found in the document")

def main():
    count_words_file(get_book_file("books/frankenstein.txt"))

main()

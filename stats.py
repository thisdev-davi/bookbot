def count_words(file):
    num_words = len(file.split())
    print(f"{num_words} words found in the document")

def get_characters(path):
    from main import get_book_file
    book = get_book_file(path).lower()
    characters = {}
    for char in book:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

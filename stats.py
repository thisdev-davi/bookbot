def get_num_words(file):
    num_words = len(file.split())
    return num_words

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

def sort_on(items):
    return items["num"]

def ordered_list(char_dict):
    list = []
    for d in char_dict:
        if d.isalpha():
            dict = {}
            dict["char"] = d
            dict["num"] = char_dict[d]
            list.append(dict)
    list.sort(reverse=True, key=sort_on)
    return list

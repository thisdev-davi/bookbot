from stats import get_characters, get_num_words, ordered_list
import sys

def get_book_file(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def main():
    if(len(sys.argv) !=2 ):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    file = get_book_file(path)
    num_words = get_num_words(file)
    char_dict = get_characters(path)
    list_char = ordered_list(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count -----")
    for l in list_char:
        print(l["char"] + ": " + str(l["num"]))
    print("============= END ===============")
    
main()

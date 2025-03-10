import sys

from stats import get_num_words
from stats import convert_lower
from stats import sort_chars

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1] #"books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at ", book_path, "...")
    print(f"----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    lowerdict = (convert_lower(text))
    #print(lowerdict)
    sorted_char_list=sort_chars(lowerdict)
    
    for lowerdict in sorted_char_list:
        char = lowerdict["char"]
        count = lowerdict["count"]
        if  char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

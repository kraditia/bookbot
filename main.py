from stats import get_num_words, get_num_char
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:     
        file_path = sys.argv[1]
        book_words = get_book_text(file_path).lower().split()

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        get_num_words(book_words)
        print("--------- Character Count -------")
        get_num_char(book_words)
    
main()

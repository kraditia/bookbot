def get_num_words(book_words):
    no_words = len(book_words)
    print(f"Found {no_words} total words")


def sort_on(items):
    return items["num"]

def get_num_char(book_words):
    freq = {} 
    for words in book_words:
        for char in words:
            freq[char] = freq.get(char,0) + 1
    
    final_dict = []
    for char in freq:
        line = {}
        line["char"] = char
        line["num"] = freq[char]
        final_dict.append(line)

    final_dict.sort(reverse=True, key=sort_on)
    for char in final_dict:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

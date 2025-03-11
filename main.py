from stats import chars_dict_to_sorted_list, num_words, word_hash
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    the_book = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    word_count = num_words(the_book)  
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_count = word_hash(the_book)
    sorted_list = chars_dict_to_sorted_list(char_count)
    for i in sorted_list:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['count']}")
    print("============= END ===============")
    


main()

import sys
from stats import  (
    count_words, 
    count_characters, 
    sort_it
)

def main():
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    path_to_book = sys.argv[1]
    contents = get_book_text(path_to_book)
    word_count = count_words(contents)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_dict = count_characters(contents)
    sorted_list = sort_it(char_dict)
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

main()
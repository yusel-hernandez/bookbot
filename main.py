from stats import get_num_words, get_num_chars, sorted_list

BOOKPATH = "./books/frankenstein.txt"


def get_book_text(filepath):
    with open(filepath) as f:
        bookstr = f.read()
        return bookstr


def print_report():
    book_text = get_book_text(BOOKPATH)
    chars_dict = get_num_chars(book_text)
    count_ordered_list = sorted_list(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {BOOKPATH}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    for item in count_ordered_list:
        if item["letter"].isalpha():
            print(f"{item['letter']}: {item['quantity']}")


def main():
    print_report()
    return


main()

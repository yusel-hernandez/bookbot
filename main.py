from stats import get_num_words, get_num_chars

BOOKPATH = "./books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        bookstr = f.read()
        return bookstr


def main():
    book_text = get_book_text(BOOKPATH)
    print(f"{get_num_words(book_text)} words found in the document")
    print(get_num_chars(book_text))
    return

main()
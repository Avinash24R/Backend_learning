def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
def number_words(text:str):
    return len(text.split())
def main():
    content = get_book_text("books/frankenstein.txt")
    words_count = number_words(content)
    print(f"Found {words_count} total words")
main()

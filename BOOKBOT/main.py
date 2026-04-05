from stats import number_words , get_char_freq , report_list
import sys


def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

def main():
    print(sys.argv)

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    content = get_book_text(path)
    words_count = number_words(content)
    freq_count = get_char_freq(content)
    sorted_char = report_list(freq_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char:
        char = item["char"]
        count = item["num"]

        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()

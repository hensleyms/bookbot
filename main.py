import sys
from stats import count_words, count_characters, sorted_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = ""

    if len(sys.argv) ==2:
        filepath = sys.argv[1]
    else:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print("Found 75767 total words")
    print("--------- Character Count -------")
    text = get_book_text(filepath)
    counts = count_characters(text)
    sorted_counts = sorted_count(counts)

    for k,v in sorted_counts.items():
        if k.isalpha():
            print(f"{k}: {v}")

    print("============= END ===============")

main()

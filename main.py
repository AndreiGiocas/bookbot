def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def number_of_words(file_contents):
    split_words = file_contents.split()
    i = 0
    for words in split_words:
        i += 1
    return i


def main():
    print(f"Found {number_of_words(get_book_text("/home/shirokets/workspace/github.com/AndreiGiocas/bookbot/bookbot/books/frankenstein.txt"))} total words")


main()
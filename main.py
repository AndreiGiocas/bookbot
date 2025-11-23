from stats import number_of_words, num_of_chars

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    number_of_characters = {}
    print(f"Found {number_of_words(get_book_text("/home/shirokets/workspace/github.com/AndreiGiocas/bookbot/bookbot/books/frankenstein.txt"))} total words")
    number_of_characters = num_of_chars(get_book_text("/home/shirokets/workspace/github.com/AndreiGiocas/bookbot/bookbot/books/frankenstein.txt"))
    print(number_of_characters)
main()
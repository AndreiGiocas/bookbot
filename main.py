from stats import number_of_words, num_of_chars, list_of_dict, sort_on

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words(get_book_text("/home/shirokets/workspace/github.com/AndreiGiocas/bookbot/bookbot/books/frankenstein.txt"))} total words")
    print("--------- Character Count -------")
    number_of_characters = num_of_chars(get_book_text("/home/shirokets/workspace/github.com/AndreiGiocas/bookbot/bookbot/books/frankenstein.txt"))
    list_nline = list_of_dict(number_of_characters)
    for nline in list_nline:
        print(f"{nline["chars"]}: {nline["num"]}")
    print("============= END ===============")

main()
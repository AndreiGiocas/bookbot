def number_of_words(file_contents):
    split_words = file_contents.split()
    i = 0
    for words in split_words:
        i += 1
    return i

def num_of_chars(file_contents):
    chars_num = {}
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    lower_file = file_contents.lower()
    for letter in lower_file:
        for lett in letters:
            if letter == lett:
                if letter not in chars_num:
                    chars_num[letter] = 1
                else:
                    chars_num[letter] = chars_num[letter] + 1
    return chars_num



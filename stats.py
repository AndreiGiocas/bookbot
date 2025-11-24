def number_of_words(file_contents):
    split_words = file_contents.split()
    i = 0
    for words in split_words:
        i += 1
    return i

def num_of_chars(file_contents):
    chars_num = {}
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","æ","â","ê","ë","ô"]
    lower_file = file_contents.lower()
    for letter in lower_file:
        for lett in letters:
            if letter == lett:
                if letter not in chars_num:
                    chars_num[letter] = 1
                else:
                    chars_num[letter] = chars_num[letter] + 1
    return chars_num

def sort_on(items):
    return items["num"]

def list_of_dict(chars_num):
    list_of_chars = []
    items = chars_num.items()
    for item in items:
        new_dict = {}
        new_dict["chars"] = item[0]
        new_dict["num"] = item[1]
        list_of_chars.append(new_dict)
    list_of_chars.sort(reverse = True, key = sort_on)
    return list_of_chars

def num_words(str_inp):
    return len(str_inp.split())

def word_hash(book):
    char_freq= {}
    for char in book:
        char_freq[char.lower()] = char_freq.get(char.lower(),0)+1
    return char_freq 

def sort_on(dict):
    return dict["count"]

def chars_dict_to_sorted_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})

    char_list.sort(reverse= True, key=sort_on)
    return char_list








def count_words(contents):
    return len(contents.split())

def count_characters(contents):
    char_dict = {}
    for c in contents.lower():
        if (c in char_dict):
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_it(char_dict):
    sorted_dict_list = []
    for k, v in char_dict.items():
        if (k.isalpha()):
            sorted_dict = {}
            sorted_dict["char"] = k
            sorted_dict["num"] = v
            sorted_dict_list.append(sorted_dict)
    sorted_dict_list.sort(reverse=True, key=sort_on)
    return sorted_dict_list
    
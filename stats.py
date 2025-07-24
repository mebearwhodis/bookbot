def get_words_count(text):
    return len(text.split())

def get_characters_dict(text):
    characters_dict = {}
    for c in text:
        char = c.lower()
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1
    return characters_dict

def sort_on(d):
    return [d["num"]]

def chars_dict_to_sorted_list(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({
            "char": char,
            "num": char_dict[char]
        })
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


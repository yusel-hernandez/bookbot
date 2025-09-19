def get_num_words(string):
    return len(string.split())


def get_num_chars(string):
    result_dict = {}
    for char in string.lower():
        num = result_dict.get(char, 0)
        result_dict.update({char: (num + 1)})
    return result_dict


def sort_on(items):
    return items["quantity"]


def sorted_list(char_dict):
    sorted = []
    for key, value in char_dict.items():
        sorted.append({"letter": key, "quantity": value})
    sorted.sort(reverse=True, key=lambda item: item['quantity'])
    return sorted

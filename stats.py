def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def count_each_character(book_text):
    char_count = {}
    for char in book_text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_list(book_text):
    unsorted_list = count_each_character(book_text)
    sorted_list = sorted(
        [{"char": char, "num": num} for char, num in unsorted_list.items()],
        key=sort_on,
        reverse=True,
    )
    return sorted_list
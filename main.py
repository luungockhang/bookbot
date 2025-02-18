def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    word_count = get_word_count(text)
    # print(f"There are {word_count} words in this text")
    character_count = count_characters(text)
    #print(character_count)
    list_of_character_count = convert_char_dictionary_to_list(character_count)
    #print(list_of_character_count)
    list_of_character_count = sort_chars_dict_by_occurence(list_of_character_count)
    #print(list_of_character_count)
    print_report(book_path,word_count,list_of_character_count)
    
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_word_count(text):
    word_count = len(text.split())
    return word_count

def count_characters(text):
    lowered_text = text.lower()
    character_counts = {}
    for character in lowered_text:
        if ((character in character_counts) == False):
            character_counts[character] = 1
        else:
            character_counts[character] += 1
    return character_counts

def sort_on(dict):
    return dict["num"]

def sort_chars_dict_by_occurence(chars):
    chars.sort(reverse=True, key=sort_on)
    return chars

def convert_char_dictionary_to_list(character_count):
    list_of_character_count = []
    for char in character_count:
        if char.isalpha():
            char_dictionary = {}
            char_dictionary["char"] = char 
            char_dictionary["num"] = character_count[char]
            list_of_character_count.append(char_dictionary)
    return list_of_character_count

def print_report(book_path, word_count, sorted_list_of_chars):
    print(f"===== Begin report of {book_path} =====")
    print(f"{word_count} found in the document")
    for char_entry in sorted_list_of_chars:
        print(f"The '{char_entry["char"]}' was found {char_entry["num"]} times")

main()
import sys
from stats import get_num_words

def main():
    if len(sys.argv) == 1:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    
    

    text = get_book_text(book_path)
    # print(text)
    word_count = get_num_words(text)
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
    print(f"{word_count} words found in the document")
    for char_entry in sorted_list_of_chars:
        print(f"'{char_entry["char"]}: {char_entry["num"]}")

main()
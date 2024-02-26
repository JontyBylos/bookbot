def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    print(print_report(book_path, number_of_words(text), sort_char(char_count(text))))

def get_book_path(path):
    with open(path) as f:
        return f.read()
    
def number_of_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    words = text.lower().split()
    letter_count = {}
    for word in words:
        for letter in word:
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

#Convert dictionary of characters and their count into a sorted list
def sort_list(dict):
    return dict["num"]

def sort_char(dict):
    char_sort = []
    for char in dict:
        char_count = dict[char]
        char_sort.append({"char": char, "num": char_count})
        
    for dict in char_sort:
        char_sort.sort(reverse=True, key=sort_list)
        
    return char_sort
    
#Aggregate all the word and character data into a report that we can print to the console
def print_report(path, number_of_words, ordered_list):
    
    print(
        f"--- Begin report of {path} ---\n"
        f"{number_of_words} words found in the document\n\n"
    )
    for item in ordered_list:
        print(f"The {item['char']} character was found {item['num']} times\n")
    
    return f"Print report for {path} Completed"

main()
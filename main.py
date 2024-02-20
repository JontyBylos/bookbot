def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    print("Number of words:", number_of_words(text))
    print("Unique characters and their count: \n", let_count(text))


def get_book_path(path):
    with open(path) as f:
        return f.read()
    
    
def number_of_words(text):
    words = text.split()
    return len(words)


#Add dictionary where lower-case letter : count
def let_count(text):
    words = text.lower().split()
    letter_count = {}

    for word in words:
        for letter in word:
        
            letter_count[letter] = letter_count.get(letter, 0) + 1

    return letter_count
    

main()




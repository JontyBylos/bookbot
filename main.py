def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    
    #Add dictionary where lower-case letter : count
    def let_count():
        words = file_contents.lower().split()
        letter_count = {}

        for word in words:
            for letter in word:
            
                letter_count[letter] = letter_count.get(letter, 0) + 1
    
        print(letter_count)
    
    let_count()

main()




def main():
    bookPath = "books/frankenstein.txt"
    text = get_book_text(bookPath)
    count = countWords(text)
    print(count)

def get_book_text(bookPath):
    with open(bookPath) as f:
        return f.read()
    
def countWords(text):
    words = text.split()
    return len(words)

def countUnique(text):
    words = text.split().lower()
    print(words)
    
main()

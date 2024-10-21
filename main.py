def main():
    bookPath = "books/frankenstein.txt"
    text = get_book_text(bookPath)
    count = countWords(text)
    unique_dict = countUnique(text)
    chars_sorted_list = chars_dict_to_sorted_list(unique_dict)
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

def get_book_text(bookPath):
    with open(bookPath) as f:
        return f.read()
    
def countWords(text):
    words = text.split()
    return len(words)

def countUnique(text):
    uniqueChar = {}
    for word in text:
        character = word.lower() 
        if character not in uniqueChar:
            uniqueChar[character] = 1
        else:
            uniqueChar[character] += 1
    return uniqueChar

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(unique_dict):
    sorted_list = []
    for character in unique_dict:
        sorted_list.append({"char": character, "num": unique_dict[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()

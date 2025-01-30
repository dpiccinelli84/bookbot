def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    words = file_contents.split()    
    words_count = count_words(words)
    chars_count = count_characters(file_contents)
    report = create_report(chars_count)
    print_report(report)
    
def create_report(chars_dict):
    report = []
    char_count = {}
    for char in chars_dict:
       if char.isalpha():
            char_count = {}
            char_count["char"] = char
            char_count["count"] = chars_dict[char]
            report.append(char_count)
    report.sort(reverse=True, key=sort_on)
    return report

def sort_on(dict):
    return dict["count"]

def print_report(report):
    for char_count in report:
        character = char_count["char"]
        times = char_count["count"]
        print(f"The '{character}' character occurs {times} times")
    return

def count_characters(book):
    lowered_book = book.lower()
    chars = {}
    for char in lowered_book:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars   
    
def count_words(book):
    return len(book)
    
main()
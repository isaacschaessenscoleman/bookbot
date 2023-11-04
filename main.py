with open('/home/isaacschaessenscoleman/workspace/github.com/bookbot/books/frankenstein.txt') as f:
    file_contents = f.read()

def count_words(file):
    file_string = str(file)
    file_list = file_string.split()
    return len(file_list)

def count_letters(file):
    dict = {}
    file_string = str(file)
    for i in file_string:
        char = i.lower()
        dict[char] = dict.get(char,0) + 1
    return dict

def print_report(file):
    print(f'{count_words(file)} words found in the document')
    print()
    letters_dict = count_letters(file)
    sorted_list = sorted(letters_dict.items(), key = lambda x:x[1], reverse = True)
    for i in sorted_list:
        if i[0].isalpha():
            print(f'The {i[0]} character was found {i[1]} times')

print_report(file_contents)
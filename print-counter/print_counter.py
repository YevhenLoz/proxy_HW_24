import sys
from collections import Counter


def my_print(*args, end='\n', sep=' '):
    output = sep.join(map(str, args)) + end
    sys.stdout.write(output)


def count_letters(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        text = ''.join(char if char.isalpha() else '' for char in text)
        text = text.lower()
        letter_counts = Counter(text)
        return letter_counts


if __name__ == '__main__':
    my_print('Hello World! ')
    letters_count = count_letters('text.txt')
    my_print(letters_count)

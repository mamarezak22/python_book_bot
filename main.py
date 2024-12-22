class Book():
    def __init__(self, path):

        self.path = path

    def read(self):
        with open(self.path, 'r') as f:
            content = f.read()
        return content

    def word_count(self):
        content = self.read()  # calling a method from a method
        words = content.split()
        return len(words)

    def char_count(self):
        content = self.read()
        content = content.lower()
        list_chars = [char for char in content if char.isalpha()]
        list_unique_chars = list(set(list_chars))
        list_unique_chars.sort()
        char_count = dict()
        for char in list_unique_chars:
            char_count[char] = list_chars.count(char)
        for char in char_count:
            print(f'The {char} character was found {char_count[char]} times.')


frankerstin_book = Book("books/frankenstein.txt")
# print(frankerstin_book.word_count())
print(frankerstin_book.char_count())

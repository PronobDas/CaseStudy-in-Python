import Read
import Word_Count
import os
book_dir = "./books"

print(os.listdir(book_dir))
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            print(inputfile)
            text = Read.read_book(inputfile)
            (num_unique, counts) = Word_Count.word_stats(Word_Count.count_words(text))
            print(num_unique)



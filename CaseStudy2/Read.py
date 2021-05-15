def read_book(title_path):
    """
    :param title_path:
    :return str:
    Read a book and returns it as a string.
    """
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r","")
    return text


text = read_book("Books/English/shakespeare/Romeo and Juliet.txt")
#print(len(text))

ind = text.find("What's in a name?")
#print(text[ind:ind+500])

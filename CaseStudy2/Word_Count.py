from collections import Counter
text = "Hello, this is Pronob Das."


def count_words(text):
    """
    :param text:
    :return dict:
    This function counts the no of words in a text having the words
    as key and the frequencies as value.
    """
    text = text.lower()
    skips = [",", ".", ";", ":", "?", '"']
    for char in skips:
        text = text.replace(char, "")

    word_count = {}
    for word in text.split(" "):
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def count_words_fast(text):
    """
    :param text:
    :return dict:
    This function counts the no of words in a text having the words
    as key and the frequencies as value.
    """
    text = text.lower()
    skips = [",", ".", ";", ":", "?", '"']
    for char in skips:
        text = text.replace(char, "")

    word_count = Counter(text.split(" "))
    return word_count


print(count_words_fast(text))

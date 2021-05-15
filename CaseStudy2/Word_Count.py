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


wc = count_words_fast(text)


def word_stats(word_counts):
    """
    :param word_counts:
    :return:
    returns number of unique words and work freq.
    """
    num_unique = len(word_counts)
    counts = word_counts.values()
    return num_unique, counts


(num_unique, counts) = word_stats(wc)
#print(num_unique)
#print(sum(counts))
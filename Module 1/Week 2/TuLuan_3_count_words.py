def read_file(file_name):
    """
    Read the content of a file
    :param file_name:
    :return:
    """
    with open(file_name, 'r') as f:
        return f.read()


def count_words(file_name):
    """
    Count the number of words in a file (lowercase and uppercase words are considered the same)
    :param file_name:
    :return:
    """
    text = read_file(file_name)
    text = text.lower()
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

if __name__ == "__main__":
    file_name = "P1_data.txt"
    print(count_words(file_name))
def read_file(file_name):
    """
    Read the content of a file
    :param file_name:
    :return:
    """
    with open(file_name, 'r') as f:
        return f.read()


def count_word(file_path):
    text = read_file(file_path)
    text = text.lower()
    words = text.split()
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    return counter

file_path = 'P1_data.txt '
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])

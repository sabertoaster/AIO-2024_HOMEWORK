def count_char_in_dict(word):
    diction = {}
    for char in word:
        if char in diction:
            diction[char] += 1
        else:
            diction[char] = 1
    return diction

if __name__ == '__main__':
    # Test 1
    word = "hello"
    print(count_char_in_dict(word))

    # Test 2
    word = "world"
    print(count_char_in_dict(word))

    # Test 3
    word = "python"
    print(count_char_in_dict(word))
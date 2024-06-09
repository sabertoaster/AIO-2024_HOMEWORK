def character_count(word):
    character_statistic = {}

    # Your Code Here
    for char in word:
        if char in character_statistic:
            character_statistic[char] += 1
        else:
            character_statistic[char] = 1
    # End Code Here

    return character_statistic


assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('smiles'))

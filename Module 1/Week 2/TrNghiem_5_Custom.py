def check_the_number(N):
    list_of_numbers = []

    results = ""
    for i in range(1, 5):
        list_of_numbers.append(i)
    if N in list_of_numbers:
        results = "True"
    if N not in list_of_numbers:
        results = "False"
    return results


N = 7
assert check_the_number(N) == "False"
N = 2
results = check_the_number(N)
print(results)

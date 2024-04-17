def sort_strings_by_length(strings):
    sorted_by_length_asc = sorted(strings, key=len)
    print("Сортировка по длине строк по возрастанию:", sorted_by_length_asc)

    sorted_by_length_desc = sorted(strings, key=len, reverse=True)
    print("Сортировка по длине строк по убыванию:", sorted_by_length_desc)

strings = ["apple", "banana", "orange", "kiwi", "grape"]
sort_strings_by_length(strings)
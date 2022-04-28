def check_word(user_input):
    user_input = user_input.lower()
    count_data = {
        "good bye":      0,
        "close":         0,
        "exit":          0,
        "show all":      0,
        "note":          0,
        "add_note":      0,
        "add_tag":       0,
        "hello":         0,
        "edit_note":     0,
        "edit_tag":      0,
        "del_note":      0,
        "del_tag":       0,
        "del_subject":   0,
        "add":           0,
        "find_note":     0,
        "find_tag":      0
    }

#####################################  ПРОВЕРКА ПО ИНДЕКСАМ

    for key,value in count_data.items():
        count = 0

        smaller_word = len(user_input)
        if len(key) < smaller_word : smaller_word = len(key)

        for i in range(0, smaller_word):
            if user_input[i] == key[i]:
                count += 1

        count_data[key] = count
    result = key
    for key, value in count_data.items():
        if value > count_data[result]:
            result = key

#####################################  ПРОВЕРКА ПО ВХОЖДЕНИЮ

    input_symbol_list = []
    for i in user_input: input_symbol_list.append(i)
    for key, value in count_data.items():
        symbol_list = []
        for i in key:
            symbol_list.append(i)
        len_symbol_list = len(symbol_list)
        len_input_symbol_list = len(input_symbol_list)

        len_smaller_list = len_symbol_list
        if len_input_symbol_list < len_symbol_list: len_smaller_list = len_input_symbol_list
        temporary_input_symbol_list = input_symbol_list
        for i in range(0, len_smaller_list):
            if temporary_input_symbol_list[i] in symbol_list:
                symbol_list.remove(temporary_input_symbol_list[i])
                count_data[key] += 1

    result = key
    for key, value in count_data.items():
        if value > count_data[result]:
            result = key

    sum_points = 0
    for i in count_data: sum_points += count_data[i]
    if sum_points == 0:
        result = 'Non matches'
        print(result)
    elif key_input.lower() == result:
        result = 'Its ok'
        print(result)
    else:
        result = f'Maybe {result}?'
        print(result)

    return result


#while True:
    #key_input = input('input')
    #check_word(key_input)
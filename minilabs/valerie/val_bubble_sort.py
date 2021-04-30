
def sort(input_list, sorting_method):

    result = []

    a_list = input_list.split(',')
    map_object = map(int, a_list)
    num_list = list(map_object)

    number_of_items = int(len(num_list))

    if sorting_method == '1':
        position = 0
        Pass = 0
        counter = 1
        while counter == 1:
            number_of_swaps = 1
            counter2 = 0
            permanent_numbers = []
            while number_of_swaps > 0:
                counter2 = counter2 + 1
                number_of_swaps = 0
                while position < number_of_items - 1:
                    if int(num_list[position]) > int(num_list[position + 1]):
                        number_of_swaps = number_of_swaps + 1
                        item1 = int(num_list[position])
                        item2 = int(num_list[position + 1])
                        num_list[position] = item2
                        num_list[position + 1] = item1
                    position = position + 1
                Pass = Pass + 1
                print('pass', Pass, ':', num_list)
                result.append('pass {Pass} : {num_list}'
                              .format(Pass=Pass, num_list=num_list))
                position = 0
                if Pass == number_of_items - 1:
                    number_of_swaps = 0
                permanent_numbers.append(num_list[number_of_items - counter2])
            if number_of_swaps == 0:
                counter = 0

        print('total number of passes:', Pass)

        if sorting_method == '2':
            position = 0
            Pass = 0
            counter = 1
            while counter == 1:
                number_of_swaps = 1
                while number_of_swaps > 0:
                    number_of_swaps = 0
                    while position < number_of_items - 1:
                        if int(num_list[position]) > int(num_list[position + 1]):
                            number_of_swaps = number_of_swaps + 1
                            item1 = int(num_list[position])
                            item2 = int(num_list[position + 1])
                            num_list[position] = item2
                            num_list[position + 1] = item1
                        position = position + 1
                    Pass = Pass + 1
                    print('pass', Pass, ':', num_list)
                    result.append('pass {Pass} : {num_list}'
                              .format(Pass=Pass, num_list=num_list))
                    position = 0
                if Pass == number_of_items - 1:
                    number_of_swaps = 0

            if number_of_swaps == 0:
                counter = 0

        print('total number of passes:', Pass)

    return result


# print('welcome to the automatic bubble sorter')
# inputted_list = input('please enter a list of numbers seperated by commas: ')
#
# sorting_method = input('if you would like your list to be sorted in ascending order, press 1, if you would like it '
#                        'to be sorted in descending order, press 2')
# print(list)

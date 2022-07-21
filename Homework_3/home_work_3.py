def ChaeckValIMP(some_dict: dict):
    """
    if it is not a dict msg the user
    :param some_dict: to chaeck if it is a dictuionary
    :return: NON
    """
    if not isinstance(some_dict, dict):
        raise Exception('it is not a dictunery !!!')
    if len(some_dict) < 3:
        raise Exception('dictunery not valid !!!')


def averageIMP(my_list: list) -> float:
    """
    :param my_list: list of numbers
    :return: the avrage
    """
    return sum(my_list) / len(my_list)


def medianIMP(my_list: list) -> float:
    """
    :param my_list: list of age's
    :return: the median value from the list
    """
    # sort the val's in list
    my_list.sort()
    # If the length is even then we return the average of the two mean values
    if len(my_list) % 2 == 0:
        return (averageIMP([my_list[len(my_list) // 2], my_list[len(my_list) // 2 - 1]]))

    # length is not even and there is one middle value
    return (my_list[len(my_list) // 2])


def split_male_female(data: dict) -> list:
    """
    splet the data to two dict's for male and female
    :param data - dict of all the data male and female
    :return - list of dict's that one is all the male and the second female
    """
    # check valid param
    ChaeckValIMP(data)

    male_dict = {}
    female_dict = {}

    for item in data:
        if data[item]["gender"] == "male":
            male_dict[item] = data[item]
        else:
            female_dict[item] = data[item]

    return [male_dict, female_dict]


def find_median_average(dict_of_vals: dict) -> list:
    """
     gives the average and the median fo vals in dict
    :param dict_of_vals: dict of numbers
    :return: list that contain the avrage and the median
    """
    # check valid param
    ChaeckValIMP(dict_of_vals)

    # creat a list of age's from the dict
    list_of_ages = []
    for item in dict_of_vals:
        list_of_ages.append(dict_of_vals[item]['age'])

    avg = averageIMP(list_of_ages)
    middel = medianIMP(list_of_ages)

    return [avg, middel]


def print_values_above(data: dict, num: int = 0):
    """
    if num = 0 print all the data in the dict else print the data when age > num
    :param data: dict of all the data
    :param num: num that present a age
    :return: NAN no return value
    """
    # check valid param
    ChaeckValIMP(data)

    if (not isinstance(num, int)) or num < 0:
        print(data)
    else:
        for k in data:
            if data[k]["age"] > num:
                print(data[k])


def main():
    data_set = {
        3322117: {
            "name": "Tal",
            "gender": "male",
            "height": 1.90,
            "age": 22
        },
        176864301: {
            "gender": "female",
            "age": 57,
            "height": 1.65,
            "name": "Anat"
        },
        176756301: {
            "gender": "female",
            "age": 80,
            "height": 1.30,
            "name": "branch"
        },
        176654301: {
            "gender": "female",
            "age": 30,
            "height": 1.65,
            "name": "hna"
        },
        176867301: {
            "gender": "male",
            "age": 37,
            "height": 1.80,
            "name": "fafu"
        },
        176826401: {
            "gender": "female",
            "age": 19,
            "height": 1.65,
            "name": "roza"
        },
        176864551: {
            "gender": "male",
            "age": 25,
            "height": 1.85,
            "name": "victor"
        },
        165864651: {
            "gender": "female",
            "age": 41,
            "height": 1.68,
            "name": "banana"
        },
        176436301: {
            "gender": "male",
            "age": 15,
            "height": 1.65,
            "name": "banani"
        }
    }

    print("\nDATA FROM DICT OVER AGE 30 (you can change it) : \n")
    print_values_above(data_set, 30)

    print(f"\nthe avg is the first and the second is the median{find_median_average(data_set)}\n")
    print(
        f"the male dict is: \n{split_male_female(data_set)[0]} \n\n dict of female is: \n{split_male_female(data_set)[1]}")


if __name__ == '__main__':
    main()

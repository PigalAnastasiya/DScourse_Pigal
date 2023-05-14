"""
Sort list by ascending items
    :parametr my_list: list-input value
    :return mylist: list
    """
def sort_list(my_list):
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i] > my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
    return my_list
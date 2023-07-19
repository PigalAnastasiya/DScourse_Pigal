"""    
 Finding odd items in a list
    :param  my_list: list - input value
    :return:list
"""  

def odd_list (my_list):
    odd_number = []
    for i in range(len(my_list)):
        if my_list[i] % 2 != 0:
            odd_number.append(my_list[i])
    return odd_number                
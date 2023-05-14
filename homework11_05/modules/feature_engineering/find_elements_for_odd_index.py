"""
Finding elements that stand in odd positions
    :param my_list - input value
    :return: list
    """
def odd_index_list(my_list):
    odd_index = []
    for i in range(len(my_list)):
        if i % 2 != 0:
            odd_index.append(my_list[i])
    return odd_index 
from modules.feature_engineering import sort_list
from modules.feature_engineering import odd_index_list
from modules.feature_engineering import odd_list
from modules.feature_engineering import file_writting

my_list = [2, 45, 3, -7, -4, 0, 6, 1, 90, -5, -7]
print(sort_list(my_list))
print(odd_index_list(my_list))
print(odd_list(my_list))
file_writting('./homework11_05/data/odd_number.txt', 'w', odd_list(my_list))
file_writting('./homework11_05/data/odd_index.txt',
              'w', odd_index_list(my_list))

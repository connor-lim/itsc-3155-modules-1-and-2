def get_unique_list(list):
    temp_list = []
    for x in list:
        count = temp_list.count(x)
        if count == 0:
            temp_list.append(x)
        
    return temp_list

my_list = [1,2,3,2,1,4]
unique_list = get_unique_list(my_list)
print(unique_list)
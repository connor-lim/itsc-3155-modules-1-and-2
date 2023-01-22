def get_combined_dict(a,b):
    combine = {}
    for x in a:
        if x in b:
            combine.update({x : a[x] + b[x]})

    return combine

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)
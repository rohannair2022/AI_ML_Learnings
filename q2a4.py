input_1 = input().split()
building_name = int(input_1[0])
routes_number = int(input_1[1])

dict_add = dict()
for i in range(routes_number):
    input_2 = input().split()
    building_1 = int(input_2[0])
    building_2 = int(input_2[1])

    if building_2 in dict_add.keys():
        dict_add[building_2].add(building_1)
    else:
        dict_add[building_2] = set()
        dict_add[building_2].add(building_1)
        dict_add[building_2].add(building_2)

dict_add_update = dict()
for key, values in dict_add.items():
    for i in values:
        if i in dict_add.keys() and key != i:
            if key in dict_add_update.keys():
                dict_add_update[key].update(values.union(dict_add[i]))
            else:
                dict_add_update[key] = set()
                dict_add_update[key].update(values.union(dict_add[i]))

max_keys = max(dict_add_update, key=dict_add_update.get)
max_value = len(dict_add_update[max_keys])

group_max_keys = set()
final_keys = []
for key, value in dict_add_update.items():
    if len(value) == max_value:
        group_max_keys.add(key)
        final_keys = list(group_max_keys)
        final_keys.sort()

print(max_value)
for i in final_keys:
    print(i,end=" ")

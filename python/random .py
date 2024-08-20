import random

def create_groups(group1, group2, group, num):
    for _ in range(len(group)):
        random_index = random.randint(0,len(group)-1)
        random_item = group.pop(random_index)
        if(len(group1) < num ):
            group1.append(random_item)
        else:
            group2.append(random_item)
        group1.sort()
        group2.sort()

if __name__ == '__main__':
    group=["A","B","C","D","E","F"]

    division_type = random.randint(0,1)

    result_group1=[]
    result_group2=[]

    if division_type == 0:
        create_groups(result_group1, result_group2, group, 4)
    if division_type == 1:
        create_groups(result_group1, result_group2, group, 2)

    print(result_group2)
    print(result_group1)
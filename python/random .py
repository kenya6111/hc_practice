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

    division_type = random.randint(3,4)

    result_group1=[]
    result_group2=[]

    create_groups(result_group1, result_group2, group, division_type)

    print(result_group2)
    print(result_group1)
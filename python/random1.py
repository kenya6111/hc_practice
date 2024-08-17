import random

def create_three_on_three(three_group1,three_group2,group):
    for _ in range(len(group)):
        random_index = random.randint(0,len(group)-1)
        random_item = group[random_index]
        if(len(three_group1) < 3 ):
            three_group1.append(random_item)
            group.pop(random_index)
        else:
            three_group2.append(random_item)
            group.pop(random_index)

def create_two_on_four(two_group,four_group,group):
    for _ in range(len(group)):
        random_index = random.randint(0,len(group)-1)
        random_item = group[random_index]
        if(len(two_group) < 2 ):
            two_group.append(random_item)
            group.pop(random_index)
        else:
            four_group.append(random_item)
            group.pop(random_index)

group=["A","B","C","D","E","F"]

three_in_three=False
two_in_four=False
division_type =random.randint(0,1)
print("division_type={}".format(division_type))
#print(len(group))
#random_index =random.randint(0,len(group)-1)
#print(random_index)

#group.pop(random_index)
#print(group)
print(group)
three_group1=[]
three_group2=[]
two_group=[]
four_group=[]

if ( division_type == 0 ):
    create_three_on_three(three_group1, three_group2, group)

if ( division_type == 1 ):
    create_two_on_four(two_group, four_group, group)


print("result!!!")
print(three_group1)
print(three_group2)
print(two_group)
print(four_group)

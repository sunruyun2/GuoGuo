import random

def swap(my_list,index1,index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def selection_sort(my_list):
    for i in range(len(my_list)):
        min = float('inf')
        min_index = i
        for j in range(i,len(my_list)):
            if my_list[j] < min:
                min = my_list[j]
                min_index = j
        swap(my_list,i,min_index)


# generate test case
def generate_my_list():
    my_list = []
    for i in range(0,100):
        my_list.append(i)

    for i in range(0,50):
        swap(my_list,random.randint(0,99),random.randint(0,99))

    return my_list


# generate check function
def check_list_sorted(my_list):
    selection_sort(my_list)
    for i in range(0,99):
        if my_list[i+1] < my_list[i] !=1:
            print("false")
    print("true")
        

# check if the test passes
for i in range(10):
    my_list = generate_my_list()
    # print(my_list)
    check_list_sorted(my_list)
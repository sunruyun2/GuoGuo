import random


def swap(my_list,index1,index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list,left,right):
    swap_index = left
    pivot_index = left
    for i in range(left+1,right+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index +=1
            swap(my_list,i,swap_index)
    swap(my_list,pivot_index,swap_index)
    return swap_index

def quick_sort_helper(my_list,left,right):
    if left < right:
        pivot_index = pivot(my_list,left,right)
        quick_sort_helper(my_list,left,pivot_index)
        quick_sort_helper(my_list,pivot_index+1,right)
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list,0,len(my_list)-1)




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
    quick_sort(my_list)
    for i in range(0,99):
        if my_list[i+1] < my_list[i] !=1:
            print("false")
    print("true")
        

# check if the test passes
for i in range(10):
    my_list = generate_my_list()
    print(my_list)
    check_list_sorted(my_list)
from textwrap import dedent


input_list1 = [1, 2, 3, 4, 5, 6]

input_list2 = [89, 2354, 3546, 23, 10, -923, 823, -12]

input_list3 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

def get_length(input_list):
    list_counter=0
    for items in input_list: 
        list_counter = list_counter +1
    return list_counter


def reverse_list(source_list, size):
    temp_size = size -1
    target_list = [None] * size
    for idx, val in enumerate(source_list):
        target_list[temp_size-idx] =val
    return target_list

def custom_print(print_input, item, listNumber):
    if listNumber != "NONE":
        print(dedent(f"""
        ====================================================================
                            {listNumber}
        ====================================================================
        """))
        
    print(dedent(f"""
    *******************************
    {item} : {print_input}
    *******************************
    """))


if __name__ == '__main__':
    list1_size = get_length(input_list1)
    custom_print(input_list1,"Original List 1", "Reverse List 1")
    custom_print(list1_size,"List 1 Size", "NONE")
    custom_print(reverse_list(input_list1,list1_size),"Target List  1", "NONE")

    list2_size = get_length(input_list2)
    custom_print(input_list2,"Original List 2", "Reverse List 2")
    custom_print(list2_size,"List 2 Size", "NONE")
    custom_print(reverse_list(input_list2,list2_size),"Target List  2", "NONE")
   
    list3_size = get_length(input_list3)
    custom_print(input_list3,"Original List 3", "Reverse List 3")
    custom_print(list3_size,"List 3 Size", "NONE")
    custom_print(reverse_list(input_list3,list3_size),"Target List  3", "NONE")
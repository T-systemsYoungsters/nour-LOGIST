import random
 
def selection_sort(list):
    run_times_insideloop=0
    run_times_outsideloop=0
    for cur_pos in range(len(list)):
        run_times_outsideloop +=1
        min_pos = cur_pos

        for scan_pos in range(cur_pos + 1, len(list)):
            run_times_insideloop +=1
            if list[scan_pos] < list[min_pos]:
                min_pos = scan_pos

        temp = list[min_pos]
        list[min_pos] = list[cur_pos]
        list[cur_pos] = temp
    print("The inside loop has runed",run_times_insideloop," times")
    print("The outside loop has runed",run_times_outsideloop," times")
 
def insertion_sort(list):
    run_times_insideloop=0
    run_times_outsideloop=0

    for key_pos in range(1, len(list)):
        run_times_outsideloop +=1
        key_value = list[key_pos]
        scan_pos = key_pos - 1
 
        while (scan_pos >= 0) and (list[scan_pos] > key_value):
            run_times_insideloop +=1
            list[scan_pos + 1] = list[scan_pos]
            scan_pos = scan_pos - 1
 
        list[scan_pos + 1] = key_value
    print("The inside loop has run",run_times_insideloop," times")
    print("The outside loop has run",run_times_outsideloop," times")

def print_list(list):
    for item in list:
        print("{:3}".format(item), end="")
    print()
 
list1 = []
list2 = []
list_size = 100
for i in range(list_size):
    new_number = random.randrange(100)
    list1.append(new_number)
    list2.append(new_number)
 
# Print the original list
print_list(list1)
 
# Use the selection sort and print the result
print("Selection Sort")
selection_sort(list1)
print_list(list1)
 

# Use the insertion sort and print the result
print("Insertion Sort")
insertion_sort(list2)
print_list(list2)